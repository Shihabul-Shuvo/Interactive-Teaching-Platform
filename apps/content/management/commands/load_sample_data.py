"""
Management command to load sample data for the Interactive Teaching Platform.

Usage:
    python manage.py load_sample_data
"""

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.content.models import MediaItem, Article, Section, Term


class Command(BaseCommand):
    help = 'Load sample data for the Interactive Teaching Platform'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        MediaItem.objects.all().delete()
        Article.objects.all().delete()
        Term.objects.all().delete()
        Section.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✓ Database cleared'))
        
        # Create sample media items
        media_items = self._create_media_items()
        
        # Create articles with sections and terms
        self._create_articles(media_items)
        
        self.stdout.write(self.style.SUCCESS('\n✅ Sample data loaded successfully!'))

    def _create_media_items(self):
        """Create sample multimedia items."""
        self.stdout.write('\nCreating multimedia items...')
        
        media_data = [
            {
                'key': 'youtube',
                'title': 'ভিডিও প্রতিবেদনে',
                'media_type': 'youtube',
                'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                'description': 'এআই এবং রোবট প্রযুক্তি সম্পর্কিত ভিডিও প্রতিবেদন',
            },
            {
                'key': 'robot',
                'title': 'রোবট',
                'media_type': 'image',
                'description': 'এআই দ্বারা চালিত রোবট যা বিভিন্ন কাজ সম্পাদন করতে সক্ষম',
            },
            {
                'key': 'omniverse',
                'title': 'ওমনিভার্স প্ল্যাটফর্ম',
                'media_type': 'text',
                'description': 'এনভিডিয়ার ওমনিভার্স প্ল্যাটফর্ম হল একটি ভার্চুয়াল পরিবেশ যেখানে রোবটগুলো বাস্তব-বিশ্বের কাজের জন্য প্রশিক্ষণ দেওয়া যায়।',
            },
            {
                'key': 'blackwell',
                'title': 'ব্ল্যাকওয়েল আল্ট্রা চিপ',
                'media_type': 'text',
                'description': 'ব্ল্যাকওয়েল আল্ট্রা হল এনভিডিয়ার সর্বশেষ প্রসেসর যা রোবটিক্স এবং এআই অ্যাপ্লিকেশনগুলির জন্য অভূতপূর্ব কর্মক্ষমতা প্রদান করে।',
            },
        ]
        
        media_items = {}
        for item in media_data:
            key = item.pop('key')
            media_obj, created = MediaItem.objects.get_or_create(
                title=item['title'],
                defaults=item
            )
            media_items[key] = media_obj
            status = '✓ Created' if created else '✓ Exists'
            self.stdout.write(f'  {status}: {media_obj.title} [{media_obj.media_type}]')
        
        return media_items

    def _create_articles(self, media_items):
        """Create sample articles with sections and terms."""
        self.stdout.write('\nCreating articles...')
        
        article_data = {
            'title': 'ফিজিক্যাল এআই যুগে পা দিচ্ছে এনভিডিয়া কৃত্রিম বুদ্ধিমত্তা',
            'subtitle': 'এনভিডিয়া ভার্চুয়াল প্রশিক্ষণ প্ল্যাটফর্ম ব্যবহার করে স্মার্ট রোবট তৈরি করছে',
            'body': '''এআইকে বাস্তব জীবনে ছড়িয়ে দিতে 'ফিজিক্যাল এআই' নিয়ে কাজ করছে [[nvidia-team|এনভিডিয়া কৃত্রিম বুদ্ধিমত্তা]]। [[omniverse|ওমনিভার্স প্ল্যাটফর্মে]] প্রশিক্ষিত রোবট ঘরের কাজ থেকে গাড়ি চালানো পর্যন্ত করতে পারবে। নতুন [[blackwell|'ব্ল্যাকওয়েল আল্ট্রা']] ও 'রুবিন' চিপ এই প্রযুক্তিকে আরও শক্তিশালী করবে।

এআই সমন্বিত রোবট প্রযুক্তির বিভিন্ন উদ্ভাবন উপস্থাপন করা হয়েছে। এই [[robot-tech|রোবটগুলো]] ঘর পরিষ্কার থেকে শুরু করে গাড়ি চালানো এবং বিভিন্ন কাজ সম্পাদন করতে সক্ষম। এনভিডিয়া এই ইভেন্টের অন্যতম প্রধান প্রযুক্তি প্রতিষ্ঠান হিসেবে উপস্থিত ছিল এবং তারা একটি নতুন প্ল্যাটফর্ম "ওমনিভার্স" প্রকাশ করেছে।

প্রধান প্রযুক্তিগত দিক:

• ব্ল্যাক হোয়েল আল্ট্রা - সর্বোচ্চ পারফরম্যান্স কম্পিউটিং
• রুবিন চিপ - এডজ ডিভাইস এবং রোবটিক্সের জন্য অপ্টিমাইজড
• ওমনিভার্স - ডিজিটাল টুইন এবং সিমুলেশন

এই চিপগুলো রোবটের কর্মক্ষমতা এবং বুদ্ধিমত্তা বাড়াতে সাহায্য করবে।''',
            'is_active': True,
        }
        
        article, created = Article.objects.get_or_create(
            slug='physical-ai-nvidia',
            defaults=article_data
        )
        
        status = '✓ Created' if created else '✓ Exists'
        self.stdout.write(f'  {status}: {article.title}')
        
        # Create sections
        self.stdout.write('\nCreating sections...')
        sections_data = [
            {
                'section_type': 'introduction',
                'title': 'ভূমিকা',
                'content': 'কৃত্রিম বুদ্ধিমত্তা (এআই) এবং রোবটিক্স প্রযুক্তি দ্রুত বিকশিত হচ্ছে এবং আমাদের দৈনন্দিন জীবনকে রূপান্তরিত করছে। এনভিডিয়া, বিশ্বের শীর্ষস্থানীয় প্রযুক্তি কোম্পানিগুলির মধ্যে একটি, এই বিপ্লবে অগ্রণী ভূমিকা পালন করছে। তাদের সর্বশেষ উদ্যোগ "ফিজিক্যাল এআই" প্রকৃত রোবটগুলিকে স্বয়ংক্রিয় এবং স্মার্ট করার জন্য উন্নত প্রযুক্তি ব্যবহার করে।',
                'order': 1,
            },
            {
                'section_type': 'detailed',
                'title': 'বিস্তারিত ব্যাখ্যা',
                'content': 'ফিজিক্যাল এআই হল এমন একটি প্রযুক্তি যা ডিজিটাল জগতের বুদ্ধিমত্তাকে ভৌত বিশ্বের সাথে সংযুক্ত করে। এনভিডিয়ার ওমনিভার্স প্ল্যাটফর্ম একটি ভার্চুয়াল পরিবেশ প্রদান করে যেখানে রোবটগুলি বাস্তব-বিশ্বের কাজগুলির জন্য সম্পূর্ণভাবে প্রশিক্ষণ নিতে পারে। এটি বাস্তবে ব্যয়বহুল ত্রুটিগুলি এড়ায় এবং শেখার সময় হ্রাস করে। ব্ল্যাকওয়েল এবং রুবিন চিপগুলি এই রোবটগুলিকে প্রয়োজনীয় কম্পিউটিং শক্তি সরবরাহ করে।',
                'order': 2,
            },
            {
                'section_type': 'resources',
                'title': 'প্রযুক্তিগত সম্পদ',
                'content': '• এনভিডিয়া ওমনিভার্স - ডিজিটাল টুইন এবং সিমুলেশন প্ল্যাটফর্ম\n• ব্ল্যাকওয়েল আল্ট্রা GPU - সর্বোচ্চ কর্মক্ষমতা কম্পিউটিং\n• রুবিন চিপ - এডজ এআই এবং রোবটিক্সের জন্য\n• ROS (রোবট অপারেটিং সিস্টেম) - ওপেন-সোর্স রোবটিক্স ফ্রেমওয়ার্ক\n• CUDA প্ল্যাটফর্ম - পারলেল কম্পিউটিং আর্কিটেকচার',
                'order': 3,
            },
        ]
        
        for section_data in sections_data:
            section, created = Section.objects.get_or_create(
                article=article,
                section_type=section_data['section_type'],
                defaults={
                    'title': section_data['title'],
                    'content': section_data['content'],
                    'order': section_data['order'],
                }
            )
            status = '✓' if created else '✓'
            self.stdout.write(f'  {status} {section.title}')
        
        # Create terms
        self.stdout.write('\nCreating interactive terms...')
        terms_data = [
            {
                'slug': 'nvidia-team',
                'label': 'এনভিডিয়া কৃত্রিম বুদ্ধিমত্তা',
                'media_key': 'youtube',
            },
            {
                'slug': 'omniverse',
                'label': 'ওমনিভার্স প্ল্যাটফর্মে',
                'media_key': 'omniverse',
            },
            {
                'slug': 'blackwell',
                'label': 'ব্ল্যাকওয়েল আল্ট্রা',
                'media_key': 'blackwell',
            },
            {
                'slug': 'robot-tech',
                'label': 'রোবটগুলো',
                'media_key': 'robot',
            },
        ]
        
        for term_data in terms_data:
            media_key = term_data.pop('media_key')
            media_item = media_items.get(media_key)
            term, created = Term.objects.get_or_create(
                slug=term_data['slug'],
                defaults={
                    'label': term_data['label'],
                    'media_item': media_item,
                }
            )
            status = '✓' if created else '✓'
            self.stdout.write(f'  {status} {term.label}')
