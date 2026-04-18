import asyncio
import os
import ssl
from typing import List,Any,Dict

import certifi
from dotenv import load_dotenv 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_core.documents import Document 
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_tavily import TavilyCrawl, TavilyExtract, TavilyMap

from logger import (log_info, log_success, log_error, log_warning, log_header, Colors)
load_dotenv()  # Load environment variables from .env file