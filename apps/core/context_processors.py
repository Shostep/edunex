from .models import UniversityConfig

def university_config(request):
    """Make university config available in all templates"""
    try:
        config = UniversityConfig.get()
        return {
            'university': config,
            'university_name': config.name if config.is_setup_complete else 'EduNex University',
        }
    except:
        return {
            'university': None,
            'university_name': 'EduNex University',
        }
