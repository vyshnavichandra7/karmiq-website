"""
Karmiq Multi-Language Translation System
Supports: English (en), Hindi (hi), Telugu (te)
"""

TRANSLATIONS = {
    'en': {
        # Nav
        'nav_brand': 'Karmiq',
        'nav_tagline': 'Order. Connect. Work. Grow.',
        'nav_jobs': 'Jobs',
        'nav_map': 'Map',
        'nav_dashboard': 'Dashboard',
        'nav_post_job': 'Post Job',
        'nav_logout': 'Logout',
        'nav_login': 'Login',
        'nav_register': 'Register',

        # Home
        'welcome': 'Welcome back,',
        'role_label': 'Role',
        'worker': 'Worker',
        'contractor': 'Contractor',
        'view_jobs': 'Browse Jobs',
        'view_map': 'View Map',
        'post_job': 'Post a Job',
        'all_jobs': 'All Jobs',
        'view_dashboard': 'Dashboard',
        'your_rating': 'Your Rating',
        'hired_congrats': 'Congratulations! You are hired for',
        'no_notifications': 'No new notifications',

        # Login
        'login_title': 'Welcome back',
        'login_subtitle': 'Sign in to your account',
        'name_placeholder': 'Your name',
        'password_placeholder': 'Password',
        'login_btn': 'Sign In',
        'no_account': "Don't have an account?",
        'register_link': 'Create one',
        'login_error': 'Invalid name or password',

        # Register
        'register_title': 'Create account',
        'register_subtitle': 'Join thousands of workers and contractors',
        'select_role': 'I am a...',
        'role_worker': '👷 Worker',
        'role_contractor': '🏗️ Contractor',
        'select_language': 'Preferred Language',
        'location_placeholder': 'Your city / area',
        'register_btn': 'Create Account',
        'have_account': 'Already have an account?',
        'login_link': 'Sign in',

        # Jobs
        'jobs_title': 'Available Jobs',
        'jobs_subtitle': 'Find work near you',
        'apply_btn': 'Apply Now',
        'chat_btn': 'Chat',
        'applicants_btn': 'View Applicants',
        'salary_label': 'Salary',
        'location_label': 'Location',
        'urgent_badge': 'Urgent',
        'filled_msg': 'Position filled',
        'no_jobs': 'No jobs available right now',
        'workers_needed': 'workers needed',
        'applied_count': 'applied',

        # Post Job
        'post_job_title': 'Post a Job',
        'post_job_subtitle': 'Find the right workers for your project',
        'job_title_placeholder': 'Job title (e.g. Electrician, Plumber)',
        'salary_placeholder': 'Daily wage (₹)',
        'select_location': 'Select location',
        'workers_needed_placeholder': 'Number of workers needed',
        'urgent_label': 'Mark as Urgent',
        'post_btn': 'Post Job',

        # Applicants
        'applicants_title': 'Applicants',
        'applicants_subtitle': 'People who applied for this job',
        'hire_btn': 'Hire',
        'hired_badge': '✅ Hired',
        'rate_btn': 'Submit Rating',
        'message_btn': 'Message',
        'no_applicants': 'No applicants yet',
        'status_label': 'Status',
        'rating_label': 'Rating',
        'worker_id': 'Worker ID',

        # Dashboard
        'dashboard_title': 'Dashboard',
        'dashboard_subtitle': 'Overview of your activity',
        'total_jobs': 'Total Jobs',
        'total_applications': 'Applications',
        'workers_hired': 'Workers Hired',

        # Chat
        'chat_title': 'Chat with',
        'message_placeholder': 'Type a message...',
        'send_btn': 'Send',
        'no_messages': 'No messages yet. Start the conversation!',

        # Map
        'map_title': 'Job Locations',
        'map_subtitle': 'Jobs near you in Hyderabad',

        # Language picker
        'lang_en': 'English',
        'lang_hi': 'हिंदी',
        'lang_te': 'తెలుగు',

        # Worker Dashboard
        'worker_dashboard_sub': 'Your job activity overview',
        'stat_applied': 'Jobs Applied',
        'stat_hired': 'Times Hired',
        'stat_pending': 'Pending',
        'stat_rating': 'Avg Rating',
        'my_applications': 'My Applications',
        'no_applications': 'You have not applied to any jobs yet',
    },

    'hi': {
        # Nav
        'nav_brand': 'Karmiq',
        'nav_tagline': 'आदेश. जुड़ो. काम. बढ़ो.',
        'nav_jobs': 'नौकरियाँ',
        'nav_map': 'नक्शा',
        'nav_dashboard': 'डैशबोर्ड',
        'nav_post_job': 'काम पोस्ट करें',
        'nav_logout': 'लॉगआउट',
        'nav_login': 'लॉगिन',
        'nav_register': 'रजिस्टर',

        # Home
        'welcome': 'स्वागत है,',
        'role_label': 'भूमिका',
        'worker': 'मज़दूर',
        'contractor': 'ठेकेदार',
        'view_jobs': 'नौकरियाँ देखें',
        'view_map': 'नक्शा देखें',
        'post_job': 'काम पोस्ट करें',
        'all_jobs': 'सभी नौकरियाँ',
        'view_dashboard': 'डैशबोर्ड',
        'your_rating': 'आपकी रेटिंग',
        'hired_congrats': 'बधाई हो! आपको काम मिल गया:',
        'no_notifications': 'कोई नई सूचना नहीं',

        # Login
        'login_title': 'वापसी पर स्वागत',
        'login_subtitle': 'अपने खाते में साइन इन करें',
        'name_placeholder': 'आपका नाम',
        'password_placeholder': 'पासवर्ड',
        'login_btn': 'साइन इन करें',
        'no_account': 'खाता नहीं है?',
        'register_link': 'बनाएं',
        'login_error': 'गलत नाम या पासवर्ड',

        # Register
        'register_title': 'खाता बनाएं',
        'register_subtitle': 'हजारों मज़दूरों और ठेकेदारों से जुड़ें',
        'select_role': 'मैं हूँ...',
        'role_worker': '👷 मज़दूर',
        'role_contractor': '🏗️ ठेकेदार',
        'select_language': 'पसंदीदा भाषा',
        'location_placeholder': 'आपका शहर / क्षेत्र',
        'register_btn': 'खाता बनाएं',
        'have_account': 'पहले से खाता है?',
        'login_link': 'साइन इन करें',

        # Jobs
        'jobs_title': 'उपलब्ध नौकरियाँ',
        'jobs_subtitle': 'अपने पास काम खोजें',
        'apply_btn': 'अभी आवेदन करें',
        'chat_btn': 'बात करें',
        'applicants_btn': 'आवेदक देखें',
        'salary_label': 'वेतन',
        'location_label': 'स्थान',
        'urgent_badge': 'अर्जेंट',
        'filled_msg': 'पद भर गया है',
        'no_jobs': 'अभी कोई नौकरी उपलब्ध नहीं',
        'workers_needed': 'मज़दूर चाहिए',
        'applied_count': 'आवेदन किया',

        # Post Job
        'post_job_title': 'काम पोस्ट करें',
        'post_job_subtitle': 'अपने प्रोजेक्ट के लिए सही मज़दूर खोजें',
        'job_title_placeholder': 'काम का नाम (जैसे बिजली मिस्त्री, प्लंबर)',
        'salary_placeholder': 'दैनिक मजदूरी (₹)',
        'select_location': 'स्थान चुनें',
        'workers_needed_placeholder': 'कितने मज़दूर चाहिए',
        'urgent_label': 'अर्जेंट मार्क करें',
        'post_btn': 'काम पोस्ट करें',

        # Applicants
        'applicants_title': 'आवेदक',
        'applicants_subtitle': 'इस काम के लिए आवेदन करने वाले',
        'hire_btn': 'काम दें',
        'hired_badge': '✅ काम मिल गया',
        'rate_btn': 'रेटिंग दें',
        'message_btn': 'संदेश',
        'no_applicants': 'अभी कोई आवेदक नहीं',
        'status_label': 'स्थिति',
        'rating_label': 'रेटिंग',
        'worker_id': 'मज़दूर ID',

        # Dashboard
        'dashboard_title': 'डैशबोर्ड',
        'dashboard_subtitle': 'आपकी गतिविधि का अवलोकन',
        'total_jobs': 'कुल नौकरियाँ',
        'total_applications': 'आवेदन',
        'workers_hired': 'काम दिया',

        # Chat
        'chat_title': 'बात करें',
        'message_placeholder': 'संदेश लिखें...',
        'send_btn': 'भेजें',
        'no_messages': 'अभी कोई संदेश नहीं। बात शुरू करें!',

        # Map
        'map_title': 'नौकरी की जगहें',
        'map_subtitle': 'हैदराबाद में आपके पास नौकरियाँ',

        # Language picker
        'lang_en': 'English',
        'lang_hi': 'हिंदी',
        'lang_te': 'తెలుగు',

        # Worker Dashboard
        'worker_dashboard_sub': 'आपकी नौकरी गतिविधि का अवलोकन',
        'stat_applied': 'आवेदन किए',
        'stat_hired': 'काम मिला',
        'stat_pending': 'अपेक्षित',
        'stat_rating': 'औसत रेटिंग',
        'my_applications': 'मेरे आवेदन',
        'no_applications': 'आपने अभी तक किसी नौकरी के लिए आवेदन नहीं किया',
    },

    'te': {
        # Nav
        'nav_brand': 'Karmiq',
        'nav_tagline': 'ఆర్డర్. అనుసంధానం. పని. ఎదగు.',
        'nav_jobs': 'ఉద్యోగాలు',
        'nav_map': 'మ్యాప్',
        'nav_dashboard': 'డాష్‌బోర్డ్',
        'nav_post_job': 'పని పోస్ట్ చేయి',
        'nav_logout': 'లాగ్అవుట్',
        'nav_login': 'లాగిన్',
        'nav_register': 'రిజిస్టర్',

        # Home
        'welcome': 'స్వాగతం,',
        'role_label': 'పాత్ర',
        'worker': 'కూలీ',
        'contractor': 'కాంట్రాక్టర్',
        'view_jobs': 'ఉద్యోగాలు చూడు',
        'view_map': 'మ్యాప్ చూడు',
        'post_job': 'పని పోస్ట్ చేయి',
        'all_jobs': 'అన్ని ఉద్యోగాలు',
        'view_dashboard': 'డాష్‌బోర్డ్',
        'your_rating': 'మీ రేటింగ్',
        'hired_congrats': 'అభినందనలు! మీకు పని దొరికింది:',
        'no_notifications': 'కొత్త నోటిఫికేషన్లు లేవు',

        # Login
        'login_title': 'తిరిగి స్వాగతం',
        'login_subtitle': 'మీ ఖాతాలో సైన్ ఇన్ చేయండి',
        'name_placeholder': 'మీ పేరు',
        'password_placeholder': 'పాస్‌వర్డ్',
        'login_btn': 'సైన్ ఇన్',
        'no_account': 'ఖాతా లేదా?',
        'register_link': 'సృష్టించు',
        'login_error': 'పేరు లేదా పాస్‌వర్డ్ తప్పు',

        # Register
        'register_title': 'ఖాతా సృష్టించు',
        'register_subtitle': 'వేల మంది కూలీలు మరియు కాంట్రాక్టర్లతో చేరండి',
        'select_role': 'నేను...',
        'role_worker': '👷 కూలీ',
        'role_contractor': '🏗️ కాంట్రాక్టర్',
        'select_language': 'ఇష్టమైన భాష',
        'location_placeholder': 'మీ నగరం / ప్రాంతం',
        'register_btn': 'ఖాతా సృష్టించు',
        'have_account': 'ఖాతా ఉందా?',
        'login_link': 'సైన్ ఇన్',

        # Jobs
        'jobs_title': 'అందుబాటులో ఉన్న ఉద్యోగాలు',
        'jobs_subtitle': 'దగ్గర పని కనుగొనండి',
        'apply_btn': 'ఇప్పుడే దరఖాస్తు చేయి',
        'chat_btn': 'చాట్',
        'applicants_btn': 'దరఖాస్తుదారులు చూడు',
        'salary_label': 'జీతం',
        'location_label': 'స్థానం',
        'urgent_badge': 'అర్జెంట్',
        'filled_msg': 'పోస్టు నిండిపోయింది',
        'no_jobs': 'ఇప్పుడు ఉద్యోగాలు అందుబాటులో లేవు',
        'workers_needed': 'కూలీలు కావాలి',
        'applied_count': 'దరఖాస్తు చేశారు',

        # Post Job
        'post_job_title': 'పని పోస్ట్ చేయి',
        'post_job_subtitle': 'మీ ప్రాజెక్ట్‌కు సరైన కూలీలను కనుగొనండి',
        'job_title_placeholder': 'పని పేరు (ఉదా. ఎలక్ట్రీషియన్, ప్లంబర్)',
        'salary_placeholder': 'రోజువారీ వేతనం (₹)',
        'select_location': 'స్థానం ఎంచుకో',
        'workers_needed_placeholder': 'ఎంత మంది కూలీలు కావాలి',
        'urgent_label': 'అర్జెంట్‌గా గుర్తించు',
        'post_btn': 'పని పోస్ట్ చేయి',

        # Applicants
        'applicants_title': 'దరఖాస్తుదారులు',
        'applicants_subtitle': 'ఈ పనికి దరఖాస్తు చేసిన వారు',
        'hire_btn': 'నియమించు',
        'hired_badge': '✅ నియమించబడ్డారు',
        'rate_btn': 'రేటింగ్ ఇవ్వు',
        'message_btn': 'సందేశం',
        'no_applicants': 'ఇంకా దరఖాస్తుదారులు లేరు',
        'status_label': 'స్థితి',
        'rating_label': 'రేటింగ్',
        'worker_id': 'కూలీ ID',

        # Dashboard
        'dashboard_title': 'డాష్‌బోర్డ్',
        'dashboard_subtitle': 'మీ కార్యకలాపాల అవలోకనం',
        'total_jobs': 'మొత్తం ఉద్యోగాలు',
        'total_applications': 'దరఖాస్తులు',
        'workers_hired': 'నియమించిన కూలీలు',

        # Chat
        'chat_title': 'చాట్',
        'message_placeholder': 'సందేశం టైప్ చేయండి...',
        'send_btn': 'పంపు',
        'no_messages': 'ఇంకా సందేశాలు లేవు. మాటలు మొదలుపెట్టండి!',

        # Map
        'map_title': 'ఉద్యోగ స్థానాలు',
        'map_subtitle': 'హైదరాబాద్‌లో మీ దగ్గర ఉద్యోగాలు',

        # Language picker
        'lang_en': 'English',
        'lang_hi': 'हिंदी',
        'lang_te': 'తెలుగు',

        # Worker Dashboard
        'worker_dashboard_sub': 'మీ ఉద్యోగ కార్యకలాపాల అవలోకనం',
        'stat_applied': 'దరఖాస్తు చేసిన ఉద్యోగాలు',
        'stat_hired': 'నియమించబడిన సార్లు',
        'stat_pending': 'పెండింగ్',
        'stat_rating': 'సగటు రేటింగ్',
        'my_applications': 'నా దరఖాస్తులు',
        'no_applications': 'మీరు ఇంకా ఏ ఉద్యోగానికీ దరఖాస్తు చేయలేదు',
    },
}


def get_translations(language_code):
    """Return translations for the given language code, fallback to English."""
    return TRANSLATIONS.get(language_code, TRANSLATIONS['en'])
