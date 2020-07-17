"""Supported Editors"""
EDITORS = {
    'ckeditor': {
        'v5': {
            'balloon': {
                'css': 'css/django_richtexteditor/ckeditor/v5/balloon.css',
                'js': {
                    'build': 'https://cdn.ckeditor.com/ckeditor5/15.0.0/balloon/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/balloon.js',
                }
            },
            'balloon-block': {
                'css': 'css/django_richtexteditor/ckeditor/v5/balloon-block.css',
                'js': {
                    'build': 'https://cdn.ckeditor.com/ckeditor5/15.0.0/balloon-block/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/balloon-block.js',
                }
            },
            'classic': {
                'css': 'css/django_richtexteditor/ckeditor/v5/classic.css',
                'js': {
                    'build': 'https://cdn.ckeditor.com/ckeditor5/15.0.0/classic/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/classic.js',
                }
            },
            'decoupled-document': {
                'css': 'css/django_richtexteditor/ckeditor/v5/decoupled-document.css',
                'js': {
                    'build': 'https://cdn.ckeditor.com/ckeditor5/15.0.0/decoupled-document/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/decoupled-document.js',
                }
            },
            'inline': {
                'css': 'css/django_richtexteditor/ckeditor/v5/inline.css',
                'js': {
                    'build': 'https://cdn.ckeditor.com/ckeditor5/15.0.0/inline/ckeditor.js',
                     'init-config': None,
                   'init-script': 'js/django_richtexteditor/ckeditor/v5/inline.js',
                }
            },
        },
        'v4': {
            'basic': {
                'css': 'css/django_richtexteditor/ckeditor/v4/basic.css',
                'js': {
                    'build': 'https://cdn.ckeditor.com/4.13.0/basic/ckeditor.js',
                    'init-script': 'js/django_richtexteditor/ckeditor/v4/basic.js',
                }
            },
            'full': {
            },
            'full-all': {
            },
            'standard': {
            },
            'standard-all': {
            },
        }
    },
    'tinymce': {
        'v5': {
            'XXX': {
                'css': 'css/django_richtexteditor/tinymce/v5/XXX.css',
                'js': {
                    'build': 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js',
                    'init-script': 'js/django_richtexteditor/tinymce/v5/XXX.js',
                }
            },
        }
    }
}
