import AminoLab
client = AminoLab.Client()
client.auth(email="rolaaav11@gmail.com", password="9379992p")
clients = client.my_communities()

for name, ndc_Id in zip(clients.name, clients.ndc_Id):
    print(f"{name} >> {ndc_Id}")
    print ('---------------------------------------------------------------------')
com_id = input('Ввдедите айди соо >>>')
chats = client.my_chat_threads(ndc_Id=com_id, size="100")
for title, thread_Id in zip(chats.title, chats.thread_Id):
    print(f"{title} >> {thread_Id}")