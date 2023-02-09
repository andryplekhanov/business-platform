from app_settings.models import ContactSettings, CompanySettings, FooterPagesSet


def load_settings(request):
    return {
        'contact_settings': ContactSettings.load(),
        'company_settings': CompanySettings.load(),
        'footer_pages': FooterPagesSet.load(),
    }
