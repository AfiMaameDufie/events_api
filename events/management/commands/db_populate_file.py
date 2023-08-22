from django.core.management.base import BaseCommand

from events.models import Category, Event


class Command(BaseCommand):
    help = 'Populates the database with some sample data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Started populating the database. This will be done soon ....'))

        # Create categories
        conference = Category.objects.create(category_name='Conference')
        summit = Category.objects.create(category_name='Summit')
        hackathon = Category.objects.create(category_name='Hackathon')
        codejam = Category.objects.create(category_name='CodeJam')
        expo = Category.objects.create(category_name='Expo')
        startup_competition = Category.objects.create(category_name='StartupCompetition')
        developer_conference = Category.objects.create(category_name='DeveloperConference')
        workshop = Category.objects.create(category_name='WorkshopSession')
        meetup = Category.objects.create(category_name='Meetup')
        usergroup = Category.objects.create(category_name='UserGroup')
        online_conference = Category.objects.create(category_name='OnlineConference')
        webinar = Category.objects.create(category_name='Webinar')
        

        # Create events
        qatesting_event = Event.objects.create(
           event_name='QA Testing for Code Quality',
           event_type='CF',
           description='The event will serve as an opportunity for software engineers and developers to meet, learn, and collaborate with international thought leaders specializing in the field of agile testing. The topics that will be touched upon include holistic testing, DevOps, sustainability testing, ensemble testing, and much more.',
        )
        qatesting_event.save()
        qatesting_event.categories.add(conference)

        gitext_expo = Event.objects.create(
           event_name='Showcasing Technology and Evolving Trends',
           event_type='EX',
           description='The Largest Tech & Startup Event in the African Continent, amplifying digital aspirations and achievements.',
        )
        gitext_expo.save()
        gitext_expo.categories.add(expo)

        pyghana_meetup = Event.objects.create(
           event_name='Python Ghana Meetup',
           event_type='MT',
           description='PyGhana Meetup for networking with Python enthusiasts and learning more about the Python Programming Language.',
        )
        pyghana_meetup.save()
        pyghana_meetup.categories.add(meetup)

        linuxaccra_ug = Event.objects.create(
           event_name='Linux Accra User Group',
           event_type='UG',
           description='A group of Linux OS users',
        )
        linuxaccra_ug.save()
        linuxaccra_ug.categories.add(usergroup)

        africa_os_summit = Event.objects.create(
           event_name='African Open Source Summit',
           event_type='SM',
           description='A summit for Open Source Technology made by Africans',
        )
        africa_os_summit.save()
        africa_os_summit.categories.add(summit)

        os_hackathon = Event.objects.create(
           event_name='Open Source Hackathon',
           event_type='HK',
           description='A Hackathon for Open Source technology creators',
        )
        os_hackathon.save()
        os_hackathon.categories.add(hackathon)

        google_codejam = Event.objects.create(
           event_name='Google CodeJam for Devs',
           event_type='CJ',
           description='A Google CodeJam for Devs',
        )
        google_codejam.save()
        google_codejam.categories.add(codejam)

        african_sc = Event.objects.create(
           event_name='A competition for Startups',
           event_type='SC',
           description='A competition for startups to pitch ideas and secure funding.',
        )
        african_sc.save()
        african_sc.categories.add(startup_competition)

        linux_conf = Event.objects.create(
           event_name='Linux Conference for Developers',
           event_type='DC',
           description='Linux Conference for Developers to showcase new tools and technology.',
        )
        linux_conf.save()
        linux_conf.categories.add(developer_conference)

        rails_workshop = Event.objects.create(
           event_name='Rails Girls Workshop',
           event_type='WS',
           description='A Rails Girls Workshop to learn about Ruby on Rails and running a server.',
        )
        rails_workshop.save()
        rails_workshop.categories.add(workshop)

        igf_conf = Event.objects.create(
           event_name='Internet Governance Online Conference',
           event_type='OC',
           description='A group of Linux OS users',
        )
        igf_conf.save()
        igf_conf.categories.add(online_conference)

        postman_webinar = Event.objects.create(
           event_name='Postman Webinar',
           event_type='WB',
           description='A Webinar on Managing your APIs with Postman',
        )
        postman_webinar.save()
        postman_webinar.categories.add(webinar)

        self.stdout.write(self.style.SUCCESS('Super quick huh? Successfully populated the database :)'))
