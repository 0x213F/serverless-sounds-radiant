import boto3

def main(args):
      name = args.get("name", "Sounds Radiant")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {"body": greeting}
