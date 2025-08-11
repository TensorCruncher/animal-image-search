# Animal Image Search 🐈 🏞️ 🔎

Search through 5400 animal images (90 classes x 60 images) using text or image queries.

Results are returned with captions.

See demo on [Hugging Face Spaces](https://huggingface.co/spaces/TensorCruncher/AnimalImageSearch).

Original image dataset from [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals/). We use it with slight changes (two images changed).

# Tech

* Image embeddings created using OpenClip.
* Search provided by FAISS.
* Captions generated using BLIP.

# Scope for improvement

* Dataset can be expanded to include more images per class so as to provide richer results. 

* Dataset contains some duplicates which need to be removed.

* OpenClip with ViT-B-32 model and laion2b_s34b_b79k weights works alright for basic queries, but fails to understand more abstract queries. For example, “Tiger food” returns images of tigers and not deers etc. Using a larger model might help in this regard by embedding images and text in a richer embedding space.

* BLIP model appears to repeat last word in caption sometimes. Needs investigation. BLIP2 might provide better captions at the cost of being slower on CPU.


# Project extensions

* Audio input can be added using whisper model. Model would convert audio to text which can then be joined with existing pipeline.

* We could use an LLM as a judge to rank / grade returned results based on how closely they match the search query.
