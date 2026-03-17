"""
Settings API - language configuration
"""

from flask import request, jsonify
from . import settings_bp
from ..config import Config


@settings_bp.route('/language', methods=['GET'])
def get_language():
    """Get current language setting."""
    return jsonify({
        'success': True,
        'data': {
            'language': Config.LANGUAGE,
            'supported': ['zh', 'vi']
        }
    })


@settings_bp.route('/language', methods=['POST'])
def set_language():
    """Set language for backend prompts."""
    data = request.get_json()
    lang = data.get('language', 'zh')

    if lang not in ('zh', 'vi'):
        return jsonify({
            'success': False,
            'error': f'Unsupported language: {lang}. Supported: zh, vi'
        }), 400

    Config.LANGUAGE = lang

    return jsonify({
        'success': True,
        'data': {'language': lang}
    })
