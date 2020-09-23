from django.core.management.base import BaseCommand, CommandError
from shortur.models import MyUrl

class Command(BaseCommand):
    help = 'Refreshes all MyUrl shortcodes'
    
    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        # print(options)
        return MyUrl.objects.refresh_shortcodes()


        # for poll_id in options['poll_ids']:
        # try:
        #     poll = Poll.objects.get(pk=poll_id)
        # except Poll.DoesNotExist:
        #     raise CommandError('Poll "%s" does not exist' % poll_id)

        # poll.opened = False
        # poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))