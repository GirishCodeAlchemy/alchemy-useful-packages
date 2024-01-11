from wordcloud import WordCloud

w = WordCloud()
i = w.generate("""Developer Golang python nodejs Angular,
    frontend Backend Devops ,
    Mircoservices Docker Kubernetes kafka Elasticsearch
    Kibana Datadog Splunk""")

i.to_file("banner.png")