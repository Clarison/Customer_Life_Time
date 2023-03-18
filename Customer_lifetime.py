import json
import altair as alt
import pandas as pd
from snowflake.snowpark import functions as F
from snowflake.snowpark.session import Session
from snowflake.snowpark import version as v
from snowflake.snowpark.functions import call_udf
import streamlit as st
import snowflake.snowpark as sp
import warnings
import os
warnings.filterwarnings('ignore')
       
     
connection_parameters = {
  "account": "wh80921.us-east-2.aws",
  "user": "clarison",
  "password": "Ashwin@8767",
  "warehouse": "COMPUTE_WH",
  "database": "SNOWFLAKE_SAMPLE_DATA",
  "schema": "Public"
}
