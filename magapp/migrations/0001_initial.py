# Generated by Django 3.0 on 2020-03-22 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Categories')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Kateqori',
                'verbose_name_plural': 'Kateqoriler',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='CommentsClone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comments')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'komentklon',
                'verbose_name_plural': 'komentklonlar',
                'ordering': ('comment',),
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Tags')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Teq',
                'verbose_name_plural': 'Teqler',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('viewed', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('question_tag', models.ManyToManyField(related_name='questions', to='magapp.Tags')),
            ],
            options={
                'verbose_name': 'Sual',
                'verbose_name_plural': 'Suallar',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40, verbose_name='Product name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discountprice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(verbose_name='Description')),
                ('author', models.CharField(max_length=40, verbose_name='Author')),
                ('pagecount', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='products', to='magapp.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='products', to='magapp.Tags')),
            ],
            options={
                'verbose_name': 'produkt',
                'verbose_name_plural': 'produktlar',
                'ordering': ('product_name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='magapp.Product')),
                ('owner_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sifaris',
                'verbose_name_plural': 'Sifarisler',
                'ordering': ('owner_order',),
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comments')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replycomments', to='magapp.Question')),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replycomments', to='magapp.Comments')),
                ('usercomment', models.ManyToManyField(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'koment',
                'verbose_name_plural': 'komentlar',
                'ordering': ('comment',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('short_description', models.TextField(verbose_name='Description')),
                ('viewer', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article_comments', models.ManyToManyField(related_name='articles', to='magapp.CommentsClone')),
                ('article_tags', models.ManyToManyField(related_name='articles', to='magapp.Tags')),
            ],
            options={
                'verbose_name': 'artikl',
                'verbose_name_plural': 'artikllar',
                'ordering': ('title',),
            },
        ),
    ]
