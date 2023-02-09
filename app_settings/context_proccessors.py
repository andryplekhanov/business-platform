from app_settings.models import ContactSettings, CompanySettings, FooterPagesSet, FooterPagesLeftSet, SocialMedia


def load_settings(request):
    return {
        'contact_settings': ContactSettings.load(),
        'company_settings': CompanySettings.load(),
        'footer_pages_right': FooterPagesSet.load(),
        'footer_pages_left': FooterPagesLeftSet.load(),
        'social_media': SocialMedia.load(),
    }
