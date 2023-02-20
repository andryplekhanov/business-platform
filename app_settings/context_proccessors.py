from app_settings.models import CompanySettings, SocialMedia


def load_settings(request):
    return {
        'company_settings': CompanySettings.load(),
        'social_media': SocialMedia.load(),
    }
