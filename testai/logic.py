from llama_index import download_loader, GPTVectorStoreIndex

NotionPageReader = download_loader('NotionPageReader')

integration_token = 'secret_g8zUO81stA7IrstccLZx1wD8HOvgUZGMs6xPvkjYC4O'
page_ids = ["fb8ec872659f4aa78ef87d4ce209cbd0"]
reader = NotionPageReader(integration_token=integration_token)
documents = reader.load_data(page_ids=page_ids)

index = GPTVectorStoreIndex.from_documents(documents=documents)
query_engine = index.as_query_engine()

