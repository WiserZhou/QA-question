import os
import time
# set the api key
# os.environ["PINECONE_API_KEY"] = "99cad44f-fb02-480d-9c18-76c938c44578"
os.environ["PINECONE_API_KEY"] = "ea43e4a7-5ff9-4d6a-95f9-bc3dd0193a69"
	

pinecone_api_key = os.environ.get('PINECONE_API_KEY')
# os.environ["XDG_CACHE_HOME"] = '../'
print(os.getcwd())
import json
from pathlib import Path
from torch import cuda
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
loader = TextLoader("data/final.txt")
documents = loader.load()
print(documents)

text_splitter = RecursiveCharacterTextSplitter(separators="\n", chunk_size=1, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
print(docs)

# # embed_model_id = 'sentence-transformers/all-MiniLM-L6-v2'
# # embed_model_id = 'all-MiniLM-L6-v2'
# embed_model_id = 'BAAI/bge-large-zh-v1.5'
# device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

# embeddings = HuggingFaceEmbeddings(
#     model_name=embed_model_id,
#     model_kwargs={'device': device},
#     encode_kwargs={'device': device, 'batch_size': 32}
# )
# print("embeddings加载完成")
# # import pinecone
# from pinecone import Pinecone
# # pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY') or '99cad44f-fb02-480d-9c18-76c938c44578')
# pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

# # pinecone.init(
# #     api_key=os.environ.get('PINECONE_API_KEY') or '99cad44f-fb02-480d-9c18-76c938c44578',
# #     environment=os.environ.get('PINECONE_ENVIRONMENT') or 'gcp-starter'
# # )
# from pinecone import ServerlessSpec, PodSpec
# use_serverless = False
# if use_serverless:
#     spec = ServerlessSpec(cloud='aws', region='us-west-2')
# else:
#     # if not using a starter index, you should specify a pod_type too
#     spec = PodSpec(environment='gcp-starter')
# index_name = 'test'
# if index_name not in pc.list_indexes().names():
#     pc.create_index(
#         index_name,
#         dimension=1024,
#         metric='dotproduct',
#         spec=spec
#     )
#     # wait for index to finish initialization
#     while not pc.describe_index(index_name).status['ready']:
#         time.sleep(1)

# """
# Connect to the index.
# """
# index = pc.Index(index_name)
# print(index.describe_index_stats())


# from langchain_pinecone import PineconeVectorStore

# index_name = "test"

# docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

# # from langchain_pinecone import PineconeVectorStore

# # # index_name = "test"
# # text_field = "text"
# # # vectorstore = PineconeVectorStore(index, embeddings, text_field)
# # query = "介绍一下井冈山?"
# # # docs = vectorstore.similarity_search(
# # #     query,  # our search query
# # #     k=3  # return 3 most relevant docs
# # # )
# # docs = docsearch.similarity_search(
# #     query,  # our search query
# #     k=3  # return 3 most relevant docs
# # )
# # print(docs)
# # print(docs[0])
# # print(docs[0].page_content)