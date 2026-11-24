def generate_bucket_manifest(bucket_name: str, region: str = 'us-east-1', *, versioning: bool = False, block_public_access: bool = True, **tags: str)-> dict:
  return { 'Bucket': bucket_name, 
         'Region': region,
         'Configuration': {
           'Versioning': versioning,
           'BlockPublicAccess': block_public_access
         },
         'Tags': tags
         }

default_region_case = generate_bucket_manifest('project_reports',versioning=False, block_public_access=True)
print(f'region: ', default_region_case['Region'], '\ns3_manifest_input:', default_region_case)

keyword_only_overridden = generate_bucket_manifest('project_reports',versioning=True)
print(f'\n', keyword_only_overridden)

kwargs_tags = generate_bucket_manifest('project_reports', project_name='nexverse_learning', description='Project reports are available here')
print(f'\n', kwargs_tags)