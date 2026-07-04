def site_info(request):
    return {
        'site_name': 'Chandu Job Portal',
        'site_tagline': 'Sarkari Result & Latest Jobs',
        'contact_email': 'contact@chandujobportal.com',
        'social_links': {
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com',
            'instagram': 'https://instagram.com',
            'telegram': 'https://telegram.org',
        }
    }
