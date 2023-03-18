import json
import altair as alt
import pandas as pd
import snowflake.snowpark as sp 
from snowflake.snowpark import functions as F
from snowflake.snowpark.session import Session
from snowflake.snowpark import version as v
from snowflake.snowpark.functions import call_udf
import streamlit as st
       
