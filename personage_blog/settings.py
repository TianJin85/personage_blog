"""
Django settings for personage_blog project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#u9)a^jiyr0kslkfa*h96-gi*g7n38*cu5(ms%xdh*q^%wi!zy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'blog_app.apps.BlogAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personage_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'personage_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#      os.path.join(BASE_DIR, "blog_app/static"),
#  ]

STATIC_ROOT = os.path.join(BASE_DIR, "blog_app/static")

# 不让收集信息
SIMPLEUI_ANALYSIS = False

# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# SIMPLEUI_HOME_ICON = 'fa fa-user'

# 自定义Log
SIMPLEUI_LOGO = 'http://127.0.0.1:8000/static/blog_app/images/Log.png'

# system_keep = True
import time
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['文章管理', '代码托管', '权限认证', '其它博客'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{
        'app' :'auth',
        'name': '文章管理',
        'icon': 'fas fa-cogs',
        'models' : [{
            'name' : '添加文章',
            'icon' : 'fas fa-plus-square',
            # 'url': 'http://49.235.110.51:8000/markdowns'
            'url': 'http://127.0.0.1:8000/markdowns'
        },
        {
            'name' : '修改文章',
            'icon' : 'fas fa-pen-nib',
            'url' : 'http://49.235.110.51:8000/update'
        },
        {
            'name' : '删除文章',
            'icon' : 'fas fa-trash-alt',
            'url' : 'http://49.235.110.51:8000/delete'
        }]

    }, {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-users-cog',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }, {
        'name': '代码托管',
        'icon': 'fas fa-code-branch',
        'models': [{
            'name': '码云',
            'url': 'https://gitee.com/yxytj/events',
            'icon': 'fab fa-git-square'
        }, {
            'name': 'github',
            'url': 'https://github.com/TianJin85',
            'icon': 'fab fa-github'
        }]
    }, {
        'name': '其它博客' ,
        'icon': 'fab fa-canadian-maple-leaf',
        'models': [{
            'name': 'CSDN',
            'url': 'http://baidu.com',
            'icon': 'fab fa-keycdn'
        }]
    }]


}

