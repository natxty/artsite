# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resume'
        db.create_table('resume_resume', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('general_description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('solo_exhibitions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('group_exhibitions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('awards_residencies', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bibliography', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('current_employment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('public_collection', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('education', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('resume', ['Resume'])


    def backwards(self, orm):
        # Deleting model 'Resume'
        db.delete_table('resume_resume')


    models = {
        'resume.resume': {
            'Meta': {'object_name': 'Resume'},
            'awards_residencies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bibliography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'current_employment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'general_description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'group_exhibitions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'public_collection': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'solo_exhibitions': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['resume']