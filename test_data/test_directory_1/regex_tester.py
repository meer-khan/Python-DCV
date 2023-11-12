import sys
import pandas as pd
import FastAPI as FP
import pathlib ,os
from fastapi import FastAPI, Depends, Response, status
from typing import Union
from fastapi.middleware.cors import CORSMiddleware