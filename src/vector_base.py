from torch import cuda
from pinecone import Pinecone, Index
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import time
import os
# print(os.getcwd())
# os.environ["XDG_CACHE_HOME"] = os.getcwd()
# print(os.getenv("XDG_CACHE_HOME"))
class MyPinecone():
    api_key: str = '',
    pc: Pinecone = None,
    index: Index = None,
    embeddings: HuggingFaceEmbeddings = None,
    vectorstore: PineconeVectorStore = None,
    def __init__(self, api_key: str, index_name: str, embed_model_id: str, text_field: str):
        self.api_key = api_key
        self.pc = Pinecone(api_key=api_key)
        # set index
        time1 = time.time()
        print(f"正在获取名为{index_name}的索引……")
        # index_name = "test"
        self.index = self.pc.Index(index_name)
        print(self.index.describe_index_stats())
        time2 = time.time()
        print(f"索引设置成功！花费{time2 - time1}秒")

        # set embeddings
        time1 = time.time()
        print("正在加载embeddings……")
        device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embed_model_id,
            model_kwargs={'device': device},
            encode_kwargs={'device': device, 'batch_size': 32},
        )
        time2 = time.time()
        print(f"embeddings加载完成！花费{time2 - time1}秒")

        # init vectorstore
        time1 = time.time()
        print("正在初始化vectorstore……")
        self.vectorstore = PineconeVectorStore(self.index, self.embeddings, text_field)
        time2 = time.time()
        print(f"vector初始化完成！花费{time2 - time1}秒")
    def get_similarity(self, query: str, k: int):
        time1 = time.time()
        docs = self.vectorstore.similarity_search(
            query,  # our search query
            k=k  # return 3 most relevant docs
        )
        time2 = time.time()
        print(f"获取数据完成！花费{time2 - time1}秒")
        print(docs)
        print(docs[0].page_content)
        context = ""
        for i in range(k):
            # context += str(i + 1) + "." + docs[i].page_content.strip() + '\n'
            context += docs[i].page_content.strip() + '\n'
        return context
