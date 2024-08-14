from django.shortcuts import get_object_or_404, render, redirect
from dashboard.forms.UserAccountForm import UserAccountForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from accounts.forms.ResetPasswordForm import ResetPasswordForm

def index(request):
    user = request.user 
    account_form = UserAccountForm(instance=user)
    reset_password_form = ResetPasswordForm()
    reset_password_form.user = user
        
    return render(request, 'dashboard/index.html', {
        'page': 'account',
        'account_form': account_form,
        'reset_password_form': reset_password_form,
        })
    
def save_account(request):
    user = request.user 
    if request.method == "POST":
        account_form = UserAccountForm(request.POST, instance=user)
        if account_form.is_valid():
            account_form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('dashboard:account')
        else:
            messages.success(request, 'Error server.')
            return redirect('dashboard:account')
        
    return redirect('dashboard:account')

def reset_user_password(request):
    user = request.user 
    if request.method == "POST":
        reset_password_form = ResetPasswordForm(request.POST)
        reset_password_form.user = user
        if reset_password_form.is_valid():
            # save new password 
            new_password = reset_password_form.cleaned_data['new_password1']
            user.set_password(new_password)
            user.save()
            
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully.')
            return redirect('dashboard:account')
        else:
            account_form = UserAccountForm(instance=user)
            messages.success(request, 'Error updating password. Please check the form.')
            return render(request, 'dashboard/index.html', {
                'page': 'account',
                'account_form': account_form,
                'reset_password_form': reset_password_form,
                })
        
    return redirect('dashboard:account')