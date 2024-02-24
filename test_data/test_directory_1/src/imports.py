import sys
import re
import pathlib ,os
import pandas as pd 

from fastapi import FastAPI, Depends, Response, status
from typing import Union
from typing_extensions import Annotated
from dotenv import load_dotenv
from pydantic import BaseModel
import math as m
from pandas import (DataFrame, DateOffset)
from typing_extensions import (AbstractSet, Annotated, Literal)
from fastapi.middleware.cors import CORSMiddleware
from spdx_tools.common.spdx_licensing import spdx_licensing
from flaskapi.sqlalchemy.request import sqlalchemy_request, sqlalchemy_response
from spdx_tools.spdx.model import (
    Actor,
    ActorType,
    Checksum,
    ChecksumAlgorithm,
    CreationInfo,
    Document,
    ExternalPackageRef,
    ExternalPackageRefCategory,
    File,
    FileType,
    Package,
    PackagePurpose,
    PackageVerificationCode,
    Relationship,
    RelationshipType,
)
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.validation.validation_message import ValidationMessage
from spdx_tools.spdx.writer.write_anything import write_file