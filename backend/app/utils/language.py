"""
Language utility for multi-language support in LLM prompts and UI messages.
Supports: zh (Chinese), vi (Vietnamese)
"""

from ..config import Config

# Language instruction snippets used in LLM system prompts
LANG_INSTRUCTIONS = {
    'zh': {
        'use_language': '使用中文',
        'output_language': '请用中文输出。',
        'user_group': '用户群体为中国人，需符合北京时间作息习惯',
        'timezone_desc': '凌晨0-5点几乎无人活动，早上6-8点逐渐活跃，工作时间9-18点中等活跃，晚间19-22点是高峰期',
        'platform_names': {
            'twitter': '世界1',
            'reddit': '世界2',
        },
        # Activity descriptions
        'posted': '发布了一条帖子',
        'posted_content': '发布了一条帖子：「{content}」',
        'liked_post': '点赞了一条帖子',
        'liked_post_by': '点赞了{author}的帖子：「{content}」',
        'disliked_post': '踩了一条帖子',
        'disliked_post_by': '踩了{author}的帖子：「{content}」',
        'reposted': '转发了一条帖子',
        'reposted_by': '转发了{author}的帖子：「{content}」',
        'quoted': '引用了一条帖子',
        'quoted_by': '引用了{author}的帖子',
        'followed': '关注了用户「{name}」',
        'commented': '在{author}的帖子「{post}」下评论道：「{content}」',
        'liked_comment': '点赞了{author}的评论：「{content}」',
        'disliked_comment': '踩了{author}的评论：「{content}」',
        'searched': '搜索了「{query}」',
        'searched_user': '搜索了用户「{query}」',
        'muted': '屏蔽了用户「{name}」',
        # Progress messages
        'building_graph': '开始构建图谱...',
        'graph_created': '图谱已创建: {id}',
        'ontology_set': '本体已设置',
        'text_split': '文本已分割为 {count} 个块',
        'waiting_zep': '等待Zep处理数据...',
        'fetching_graph': '获取图谱信息...',
        'build_complete': '构建完成',
        'processing': 'Zep处理中... {done}/{total} 完成',
    },
    'vi': {
        'use_language': 'Sử dụng tiếng Việt',
        'output_language': 'Vui lòng xuất bằng tiếng Việt.',
        'user_group': 'Nhóm người dùng là người Việt Nam, cần phù hợp với thói quen sinh hoạt theo giờ Việt Nam (GMT+7)',
        'timezone_desc': '0-5 giờ sáng hầu như không hoạt động, 6-8 giờ dần hoạt động, 9-18 giờ hoạt động trung bình, 19-22 giờ là giờ cao điểm',
        'platform_names': {
            'twitter': 'Thế giới 1',
            'reddit': 'Thế giới 2',
        },
        # Activity descriptions
        'posted': 'Đã đăng một bài viết',
        'posted_content': 'Đã đăng bài viết: "{content}"',
        'liked_post': 'Đã thích một bài viết',
        'liked_post_by': 'Đã thích bài viết của {author}: "{content}"',
        'disliked_post': 'Đã không thích một bài viết',
        'disliked_post_by': 'Đã không thích bài viết của {author}: "{content}"',
        'reposted': 'Đã chia sẻ lại một bài viết',
        'reposted_by': 'Đã chia sẻ lại bài viết của {author}: "{content}"',
        'quoted': 'Đã trích dẫn một bài viết',
        'quoted_by': 'Đã trích dẫn bài viết của {author}',
        'followed': 'Đã theo dõi người dùng "{name}"',
        'commented': 'Đã bình luận trên bài viết "{post}" của {author}: "{content}"',
        'liked_comment': 'Đã thích bình luận của {author}: "{content}"',
        'disliked_comment': 'Đã không thích bình luận của {author}: "{content}"',
        'searched': 'Đã tìm kiếm "{query}"',
        'searched_user': 'Đã tìm kiếm người dùng "{query}"',
        'muted': 'Đã chặn người dùng "{name}"',
        # Progress messages
        'building_graph': 'Bắt đầu xây dựng đồ thị...',
        'graph_created': 'Đồ thị đã tạo: {id}',
        'ontology_set': 'Bản thể đã thiết lập',
        'text_split': 'Văn bản đã chia thành {count} khối',
        'waiting_zep': 'Đang chờ Zep xử lý dữ liệu...',
        'fetching_graph': 'Đang lấy thông tin đồ thị...',
        'build_complete': 'Xây dựng hoàn tất',
        'processing': 'Zep đang xử lý... {done}/{total} hoàn thành',
    }
}


def get_lang():
    """Get the current language setting."""
    return getattr(Config, 'LANGUAGE', 'zh')


def get_text(key, **kwargs):
    """Get a localized text string.

    Args:
        key: dot-separated key like 'posted_content'
        **kwargs: format parameters

    Returns:
        Localized string with parameters filled in
    """
    lang = get_lang()
    texts = LANG_INSTRUCTIONS.get(lang, LANG_INSTRUCTIONS['zh'])
    text = texts.get(key, LANG_INSTRUCTIONS['zh'].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, IndexError):
            return text
    return text


def get_platform_name(platform):
    """Get localized platform display name."""
    lang = get_lang()
    texts = LANG_INSTRUCTIONS.get(lang, LANG_INSTRUCTIONS['zh'])
    return texts.get('platform_names', {}).get(platform, platform)


def get_prompt_language_instruction():
    """Get the language instruction to prepend/append to LLM prompts."""
    lang = get_lang()
    if lang == 'vi':
        return "\n\n**IMPORTANT: You MUST respond in Vietnamese (tiếng Việt). All output text must be in Vietnamese.**\n"
    return ""  # Chinese is the default, prompts are already in Chinese
