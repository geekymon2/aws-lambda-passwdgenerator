# AWS Lambda Password Generator
This is a simple implementation of a random password generator using AWS Lambda. Depoyment into AWS is automated via GitHub Actions. AWS Lambda function is executed to run a simply python script which generates random passwords.

# Sample Request Payload
- length: lenth of the generated passwords
- count: no of passwords to generate
- digits: contain digits
- special_chars: contain special characters

```json
{
  "length": "20",
  "count": "10",
  "digits": "",
  "special_chars": "yes"
}
```

# Response Payload
```json
{
  "statusCode": 200,
  "statusMessage": "SUCCESS",
  "body": "\"[\\\"\\\\\\\"Sj>F*+[(;RJ;?xU[d%>\\\", \\\"G#|ojG\\\\\\\\BcGa/r@%<h$i~\\\", \\\"RLf*ZA=h[#oyiyE&hd:C\\\", \\\"p@IaDE'd.UmX~ei;)F-\\\\\\\"\\\", \\\"N$jzb]G%CgFy\\\\\\\"Zqw,(I\\\\\\\"\\\", \\\"*rRR,#ZK@QUF|SS_{*L?\\\", \\\"xxQiw{!VUf=pdj}vE~tS\\\", \\\"jPjDo<oBCu~h>f{BOX&B\\\", \\\"[z/nbZ&cY(G$h<f{-fYd\\\", \\\"iuh>Oh;!ett\\\\\\\"Yc^^]xiG\\\"]\""
}
```