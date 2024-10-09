# Now let's create integration_test.py

# We'll use the dataframe we created in Q3 (the dataframe for the unit test) and save it to S3. You don't need to do anything else: just create a dataframe and save it.

# We will pretend that this is data for January 2023.

# Run the integration_test.py script. After that, use AWS CLI to verify that the file was created.

# Use this snipped for saving the file:

# df_input.to_parquet(
#     input_file,
#     engine='pyarrow',
#     compression=None,
#     index=False,
#     storage_options=options
# )
# What's the size of the file?

# 3620
# 23620
# 43620
# 63620
# Note: it's important to use the code from the snippet for saving the file. Otherwise the size may be different depending on the OS, engine and compression. Even if you use this exact snippet, the size of your dataframe may still be a bit off. Just select the closest option.

import pandas as pd
from datetime import datetime
import os

AWS_ENDPOINT_URL="http://localhost:4566"
AWS_ACCESS_KEY_ID='test'
AWS_SECRET_ACCESS_KEY='test'

options = {
    'key': AWS_ACCESS_KEY_ID,
    'secret': AWS_SECRET_ACCESS_KEY,
    'client_kwargs': {
        'endpoint_url': AWS_ENDPOINT_URL
    }
}

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
]

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']

def test_s3():
    output_file=f's3://nyc-duration/q5.parquet'

    df_input = pd.DataFrame(data, columns=columns)

    df_input.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )

def test_save_data():
    input_file=f's3://nyc-duration/out/2023-01.parquet'
    df = pd.read_parquet(input_file, storage_options=options)
    assert df['predicted_duration'].sum() == 36.27725045203073
