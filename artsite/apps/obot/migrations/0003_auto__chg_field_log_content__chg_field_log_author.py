# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Log.content'
        db.alter_column('obot_log', 'content', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Log.author'
        db.alter_column('obot_log', 'author', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Log.content'
        db.alter_column('obot_log', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Log.author'
        db.alter_column('obot_log', 'author', self.gf('django.db.models.fields.TextField')())

    models = {
        'obot.log': {
            'Meta': {'object_name': 'Log'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'obot.response': {
            'Meta': {'object_name': 'Response'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['obot']