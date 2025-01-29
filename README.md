# Agentic RAG with custom Tool

### Project File Structure

```
├── config.py
├── main.py
├── README.md
├── router
│   └── routes.py
└── service
    ├── crewai
    │   ├── config
    │   │   ├── agents.yaml
    │   │   └── tasks.yaml
    │   ├── main_crew.py
    │   ├── main_crew_run.py
    │   └── tools
    │       └── vector_search.py
    └── db
        └── db.py
```


```
Result 

Generative Adversarial Networks (GANs) are a powerful class of deep learning models used to generate new data instances resembling the training data.  They consist of two neural networks: a generator and a discriminator. The generator attempts to create realistic data, while the discriminator tries to distinguish between real and generated data. This adversarial process results in the generator producing increasingly realistic outputs. GANs have proven remarkably successful in various applications, including image generation, text generation, and drug discovery. However, training GANs can be challenging, often requiring careful hyperparameter tuning and architectural design. Current research focuses on improving GAN training stability, enhancing the quality and diversity of generated data, and exploring new applications.  The ideal scenario is generating additional realistic data to aid learning, using techniques similar to those used to train the system.  This involves creating a tool that samples from a precise distribution (e.g., celebrity faces) where instances resemble or highly correlate with real samples.  Generated images should not only fit the original distribution but also add useful information like redundancy, different poses, or highly probable scenarios not present in the original dataset.  Current research trends link Deep Learning and Kernel Methods to establish a unifying theory of learning, with scaling GANs being a key frontier.

```