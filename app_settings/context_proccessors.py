from app_settings.models import CompanySettings, FooterPagesRightSet, FooterPagesLeftSet, SocialMedia


def load_settings(request):
    return {
        'company_settings': CompanySettings.load(),
        'footer_pages_right': FooterPagesRightSet.load(),
        'footer_pages_left': FooterPagesLeftSet.load(),
        'social_media': SocialMedia.load(),
    }
