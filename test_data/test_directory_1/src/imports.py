import sys
import os
import pathlib
from fastapi import FastAPI, Depends, Response, status
from typing import Union
from typing_extensions import Annotated
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware