from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def pasien_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/authentication/login/'):
    '''
    Decorator for views that checks that the logged in user type = pasien,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_pasien,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    

    # print("TES DECORATOR PASIEN")

    if function:
        # print("TES DECORATOR IN FUNCTION PASIEN")
        return actual_decorator(function)

    # print("TES DECORATOR AFTER FUNCTION PASIEN")
    return actual_decorator


def dokter_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/authentication/login/'):
    '''
    Decorator for views that checks that the logged in user type = dokter,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_dokter,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    # print("TES DECORATOR DOKTER")
    if function:
        # print("TES DECORATOR IN FUNCTION DOKTER")
        return actual_decorator(function)
    # print("TES DECORATOR AFTER FUNCTION DOKTER")
    return actual_decorator