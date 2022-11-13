# Generated by Django 4.1 on 2022-11-12 12:50

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMatchs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team', models.CharField(max_length=255)),
                ('second_team', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('tur', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryBlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='players/')),
                ('video', models.FileField(upload_to='playervideos/')),
                ('number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='team/')),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('draw', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('scored', models.IntegerField(default=0)),
                ('missed', models.IntegerField(default=0)),
                ('game', models.IntegerField(default=0)),
                ('totalgoal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Turnir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=555)),
                ('date', models.DateField()),
                ('clubs', models.ManyToManyField(to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='NextMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('stadium', models.CharField(max_length=255)),
                ('club_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_1', to='main.team')),
                ('club_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_2', to='main.team')),
                ('turnir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.turnir')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_1_result', models.IntegerField()),
                ('club_2_result', models.IntegerField()),
                ('club_1_muallif1', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif1', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif2', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif2', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif3', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif3', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif4', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif4', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif5', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif5', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif6', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif6', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif7', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif7', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif8', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif8', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif9', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif9', models.CharField(blank=True, max_length=255, null=True)),
                ('club_1_muallif10', models.CharField(blank=True, max_length=255, null=True)),
                ('club_2_muallif10', models.CharField(blank=True, max_length=255, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nextmatch')),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='blog_images/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoryblogs')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('types', models.IntegerField(blank=True, choices=[(1, 'manager'), (2, 'user')], default=2, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]