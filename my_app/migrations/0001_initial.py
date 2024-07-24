# Generated by Django 5.0.7 on 2024-07-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Changement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_impacte', models.CharField(max_length=100)),
                ('date_changement', models.DateTimeField()),
                ('duree_changement', models.DurationField()),
                ('destinataire', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('statut_changement', models.CharField(choices=[('en cours', 'En cours'), ('clôturé', 'Clôturé')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_impacte', models.CharField(max_length=100)),
                ('destinataire', models.EmailField(max_length=254)),
                ('date', models.DateTimeField()),
                ('statut', models.CharField(choices=[('en cours', 'En cours'), ('clôturé', 'Clôturé')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ITMFS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_utilisateur', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mot_de_passe', models.CharField(max_length=100)),
            ],
        ),
    ]
