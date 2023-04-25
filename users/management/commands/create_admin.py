from django.core.management.base import BaseCommand, CommandError, CommandParser
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--username", type=str, help="Define a username")
        parser.add_argument("--password", type=str, help="Define a password")
        parser.add_argument("--email", type=str, help="Define an email")

    def handle(self, *args, **kwargs) -> str:
        help = "Creates an admin user"
        my_username = kwargs["username"] or "admin"
        my_password = kwargs["password"] or "admin1234"
        my_email = kwargs["email"] or "admin@example.com"

        check_username = User.objects.filter(username=my_username).first()
        check_email = User.objects.filter(email=my_email).first()

        if check_username:
            raise CommandError(
                f"Username `{check_username.username}` already taken."
            )

        if check_email:
            raise CommandError(f"Email `{check_email.email}` already taken.")

        User.objects.create_superuser(
            username=my_username,
            password=my_password,
            email=my_email,
        )
        self.stdout.write(
            self.style.SUCCESS(f"Admin `{my_username}` successfully created!")
        )
