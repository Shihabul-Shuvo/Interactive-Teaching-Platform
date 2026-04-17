from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.content.models import MediaItem, Article, Section, Term


class Command(BaseCommand):
    help = 'Load Nvidia Physical AI article with comprehensive multimedia content'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        MediaItem.objects.all().delete()
        Article.objects.all().delete()
        Term.objects.all().delete()
        Section.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✓ Database cleared'))

        # Create multimedia items
        self.stdout.write('\nCreating multimedia items...')
        media_items = {}

        # Robot image
        robot_img = MediaItem.objects.create(
            title='রোবট',
            media_type='image',
            description='এআই দ্বারা চালিত রোবট যা বিভিন্ন কাজ সম্পাদন করতে সক্ষম'
        )
        media_items['robot'] = robot_img
        self.stdout.write(f'  ✓ রোবট [Image]')

        # Physical AI video
        physical_ai_video = MediaItem.objects.create(
            title='ফিজিক্যাল এআই',
            media_type='video',
            description='এনভিডিয়ার ফিজিক্যাল এআই প্রযুক্তির বিস্তারিত ভিডিও প্রতিবেদন'
        )
        media_items['physical_ai'] = physical_ai_video
        self.stdout.write(f'  ✓ ফিজিক্যাল এআই [Video]')

        # YouTube content
        youtube_content = MediaItem.objects.create(
            title='ভিডিও প্রতিবেদনে',
            media_type='youtube',
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            description='এআই এবং রোবট প্রযুক্তি সম্পর্কিত ভিডিও প্রতিবেদন'
        )
        media_items['youtube'] = youtube_content
        self.stdout.write(f'  ✓ ভিডিও প্রতিবেদনে [YouTube]')

        # Omniverse platform info (text)
        omniverse_text = MediaItem.objects.create(
            title='ওমনিভার্স প্ল্যাটফর্ম',
            media_type='text',
            description='এনভিডিয়ার ওমনিভার্স প্ল্যাটফর্ম হল একটি ভার্চুয়াল পরিবেশ যেখানে রোবটগুলো বাস্তব-বিশ্বের কাজের জন্য প্রশিক্ষণ দেওয়া যায়। এটি বিভিন্ন শিল্পে প্রয়োগ করা যায় যেমন স্বাস্থ্যসেবা, উৎপাদন, লজিস্টিক্স এবং খুচরা।'
        )
        media_items['omniverse'] = omniverse_text
        self.stdout.write(f'  ✓ ওমনিভার্স প্ল্যাটফর্ম [Text]')

        # Blackwell chip info (text)
        blackwell_text = MediaItem.objects.create(
            title='ব্ল্যাকওয়েল আল্ট্রা চিপ',
            media_type='text',
            description='ব্ল্যাকওয়েল আল্ট্রা হল এনভিডিয়ার সর্বশেষ প্রসেসর যা রোবটিক্স এবং এআই অ্যাপ্লিকেশনগুলির জন্য অভূতপূর্ব কর্মক্ষমতা প্রদান করে। এটি কৃত্রিম বুদ্ধিমত্তার প্রক্রিয়াকরণ ক্ষমতা পাঁচগুণ বৃদ্ধি করে।'
        )
        media_items['blackwell'] = blackwell_text
        self.stdout.write(f'  ✓ ব্ল্যাকওয়েল আল্ট্রা চিপ [Text]')

        # Create the article
        self.stdout.write('\nCreating article...')
        article_data = {
            'title': 'ফিজিক্যাল এআই যুগে পা দিচ্ছে এনভিডিয়া কৃত্রিম বুদ্ধিমত্তা',
            'subtitle': 'এনভিডিয়া ভার্চুয়াল প্রশিক্ষণ প্ল্যাটফর্ম ব্যবহার করে স্মার্ট রোবট তৈরি করছে',
            'body': '''এআইকে বাস্তব জীবনে ছড়িয়ে দিতে 'ফিজিক্যাল এআই' নিয়ে কাজ করছে এনভিডিয়া কৃত্রিম বুদ্ধিমত্তা। [[omniverse]] প্ল্যাটফর্মে প্রশিক্ষিত রোবট ঘরের কাজ থেকে গাড়ি চালানো পর্যন্ত করতে পারবে। নতুন [[blackwell]] ও 'রুবিন' চিপ এই প্রযুক্তিকে আরও শক্তিশালী করবে।

এআই সমন্বিত রোবট প্রযুক্তির বিভিন্ন উদ্ভাবন উপস্থাপন করা হয়েছে। এই [[robot-tech]] ঘর পরিষ্কার থেকে শুরু করে গাড়ি চালানো এবং বিভিন্ন কাজ সম্পাদন করতে সক্ষম। এনভিডিয়া এই ইভেন্টের অন্যতম প্রধান প্রযুক্তি প্রতিষ্ঠান হিসেবে উপস্থিত ছিল এবং তারা একটি নতুন প্ল্যাটফর্ম "ওমনিভার্স" প্রকাশ করেছে, যা একটি ভার্চুয়াল প্রশিক্ষণ ক্ষেত্র হিসেবে কাজ করবে। এই প্ল্যাটফর্মের মাধ্যমে রোবটগুলো বাস্তব বিশ্বের জন্য প্রশিক্ষিত হবে, যা তাদের দক্ষতা এবং শক্তি বাড়াতে সাহায্য করবে।

প্রধান প্রযুক্তিগত দিক:

• ব্ল্যাক হোয়েল আল্ট্রা - সর্বোচ্চ পারফরম্যান্স কম্পিউটিং
• রুবিন চিপ - এডজ ডিভাইস এবং রোবটিক্সের জন্য অপ্টিমাইজড
• ওমনিভার্স - ডিজিটাল টুইন এবং সিমুলেশন

এই চিপগুলো রোবটের কর্মক্ষমতা এবং বুদ্ধিমত্তা বাড়াতে সাহায্য করবে। এনভিডিয়ার লক্ষ্য হলো রোবটগুলোকে এমনভাবে তৈরি করা, যাতে তারা কারখানা, হাসপাতাল থেকে শুরু করে সাধারণ মানুষের বাসস্থানে কার্যকর ভূমিকা রাখতে পারে।

প্রথম চিপ প্ল্যাটফর্মটি ৫ গুণ দ্রুতগতির এবং এটি ব্যবহারকারীর জন্য আরও স্মার্ট সহকারী, নিরাপদ গাড়ি চালানো ইত্যাদি সক্ষমতা প্রদান করবে। তবে, প্রযুক্তির এই বিকাশে কিছু সীমাবদ্ধতা এবং বাধা রয়েছে, যা মূলত প্রযুক্তিগত, কোম্পানি-ভিত্তিক প্রতিযোগিতা এবং আইনি বিধিনিষেধ থেকে উদ্ভূত।

বিশেষ করে, বিশ্বজুড়ে এআই নিয়ন্ত্রণ সংক্রান্ত কঠোর আইন প্রণয়ন হচ্ছে, যা এআই প্রযুক্তির প্রভাব এবং ব্যবহারকে প্রভাবিত করছে।''',
            'is_active': True,
        }

        article = Article.objects.create(**article_data)
        self.stdout.write(f'  ✓ Article created: {article.title}')

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
            section = Section.objects.create(article=article, **section_data)
            self.stdout.write(f'  ✓ {section.title}')

        # Create terms linking to media
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
            term = Term.objects.create(media_item=media_item, **term_data)
            self.stdout.write(f'  ✓ {term.label}')

        self.stdout.write(self.style.SUCCESS('\n✅ Article and media loaded successfully!'))
