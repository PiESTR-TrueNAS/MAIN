#!/usr/bin/env python

import os
import re


# Some checkup
if 'GITHUB_WORKSPACE' in os.environ:
  WORKSPACE = os.getenv( 'GITHUB_WORKSPACE' )
else:
  WORKSPACE = '../..'



# Defining some constant
ACTION_TEMPLATE_FILE   = os.path.join( WORKSPACE, ".github/data/readme/01" )
MANIFEST_TEMPLATE_FILE = os.path.join( WORKSPACE, ".github/data/readme/template" )
REPOSITORIES_DATA_FILE = os.path.join( WORKSPACE, ".github/data/repositories.data" )
OUTPUT_FILE            = os.path.join( WORKSPACE, "ReadMe.md" )



# Reading all the files
with open( ACTION_TEMPLATE_FILE, 'r' ) as file:
  ACTION_TEMPLATE = file.read()

with open( MANIFEST_TEMPLATE_FILE, 'r' ) as file:
  MANIFEST_TEMPLATE = file.read()

with open( REPOSITORIES_DATA_FILE, 'r' ) as file:
  REPOSITORIES_DATA = file.readlines()



# Processing all data
result = ""
for repository in REPOSITORIES_DATA:
  repository = repository.rstrip()
  path = repository.split( "/", 1 )[ 1 ]

  tmp = ACTION_TEMPLATE
  tmp = tmp.replace( "{{PATH}}", repository )
  tmp = tmp.replace( "{{NAME}}", path )

  result += tmp



# Create the final file
result = result.rstrip()
MANIFEST_TEMPLATE = re.sub( '{{PLUGINS}}', result, MANIFEST_TEMPLATE )
with open( OUTPUT_FILE, 'w' ) as file:
  file.write( MANIFEST_TEMPLATE )
  print( MANIFEST_TEMPLATE )
