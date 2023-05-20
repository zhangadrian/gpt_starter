import gpt_pb2

resp = gpt_pb2.GPTResponse()
resp.reply = "test"
print(resp.reply)