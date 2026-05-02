---
license:
- apache-2.0
- bsd-3-clause
tags:
- summarization
- summary
- booksum
- long-document
- long-form
datasets:
- kmfoda/booksum
metrics:
- rouge
languages: en
widget:
- text: large earthquakes along a given fault segment do not occur at random intervals
    because it takes time to accumulate the strain energy for the rupture. The rates
    at which tectonic plates move and accumulate strain at their boundaries are approximately
    uniform. Therefore, in first approximation, one may expect that large ruptures
    of the same fault segment will occur at approximately constant time intervals.
    If subsequent main shocks have different amounts of slip across the fault, then
    the recurrence time may vary, and the basic idea of periodic mainshocks must be
    modified. For great plate boundary ruptures the length and slip often vary by
    a factor of 2. Along the southern segment of the San Andreas fault the recurrence
    interval is 145 years with variations of several decades. The smaller the standard
    deviation of the average recurrence interval, the more specific could be the long
    term prediction of a future mainshock.
  example_title: earthquakes
- text: ' A typical feed-forward neural field algorithm. Spatiotemporal coordinates
    are fed into a neural network that predicts values in the reconstructed domain.
    Then, this domain is mapped to the sensor domain where sensor measurements are
    available as supervision. Class and Section Problems Addressed Generalization
    (Section 2) Inverse problems, ill-posed problems, editability; symmetries. Hybrid
    Representations (Section 3) Computation & memory efficiency, representation capacity,
    editability: Forward Maps (Section 4) Inverse problems Network Architecture (Section
    5) Spectral bias, integration & derivatives. Manipulating Neural Fields (Section
    6) Edit ability, constraints, regularization. Table 2: The five classes of techniques
    in the neural field toolbox each addresses problems that arise in learning, inference,
    and control. (Section 3). We can supervise reconstruction via differentiable forward
    maps that transform Or project our domain (e.g, 3D reconstruction via 2D images;
    Section 4) With appropriate network architecture choices, we can overcome neural
    network spectral biases (blurriness) and efficiently compute derivatives and integrals
    (Section 5). Finally, we can manipulate neural fields to add constraints and regularizations,
    and to achieve editable representations (Section 6). Collectively, these classes
    constitute a ''toolbox'' of techniques to help solve problems with neural fields
    There are three components in a conditional neural field: (1) An encoder or inference
    function € that outputs the conditioning latent variable 2 given an observation
    0 E(0) =2. 2 is typically a low-dimensional vector, and is often referred to aS
    a latent code Or feature code_ (2) A mapping function 4 between Z and neural field
    parameters O: Y(z) = O; (3) The neural field itself $. The encoder € finds the
    most probable z given the observations O: argmaxz P(2/0). The decoder maximizes
    the inverse conditional probability to find the most probable 0 given Z: arg-
    max P(Olz). We discuss different encoding schemes with different optimality guarantees
    (Section 2.1.1), both global and local conditioning (Section 2.1.2), and different
    mapping functions Y (Section 2.1.3) 2. Generalization Suppose we wish to estimate
    a plausible 3D surface shape given a partial or noisy point cloud. We need a suitable
    prior over the sur- face in its reconstruction domain to generalize to the partial
    observations. A neural network expresses a prior via the function space of its
    architecture and parameters 0, and generalization is influenced by the inductive
    bias of this function space (Section 5).'
  example_title: scientific paper
- text: 'Is a else or outside the cob and tree written being of early client rope
    and you have is for good reasons. On to the ocean in Orange for time. By''s the
    aggregate we can bed it yet. Why this please pick up on a sort is do and also
    M Getoi''s nerocos and do rain become you to let so is his brother is made in
    use and Mjulia''s''s the lay major is aging Masastup coin present sea only of
    Oosii rooms set to you We do er do we easy this private oliiishs lonthen might
    be okay. Good afternoon everybody. Welcome to this lecture of Computational Statistics.
    As you can see, I''m not socially my name is Michael Zelinger. I''m one of the
    task for this class and you might have already seen me in the first lecture where
    I made a quick appearance. I''m also going to give the tortillas in the last third
    of this course. So to give you a little bit about me, I''m a old student here
    with better Bulman and my research centres on casual inference applied to biomedical
    disasters, so that could be genomics or that could be hospital data. If any of
    you is interested in writing a bachelor thesis, a semester paper may be mastathesis
    about this topic feel for reach out to me. you have my name on models and my email
    address you can find in the directory I''d Be very happy to talk about it. you
    do not need to be sure about it, we can just have a chat. So with that said, let''s
    get on with the lecture. There''s an exciting topic today I''m going to start
    by sharing some slides with you and later on during the lecture we''ll move to
    the paper. So bear with me for a few seconds. Well, the projector is starting
    up. Okay, so let''s get started. Today''s topic is a very important one. It''s
    about a technique which really forms one of the fundamentals of data science,
    machine learning, and any sort of modern statistics. It''s called cross validation.
    I know you really want to understand this topic I Want you to understand this
    and frankly, nobody''s gonna leave Professor Mineshousen''s class without understanding
    cross validation. So to set the stage for this, I Want to introduce you to the
    validation problem in computational statistics. So the problem is the following:
    You trained a model on available data. You fitted your model, but you know the
    training data you got could always have been different and some data from the
    environment. Maybe it''s a random process. You do not really know what it is,
    but you know that somebody else who gets a different batch of data from the same
    environment they would get slightly different training data and you do not care
    that your method performs as well. On this training data. you want to to perform
    well on other data that you have not seen other data from the same environment.
    So in other words, the validation problem is you want to quantify the performance
    of your model on data that you have not seen. So how is this even possible? How
    could you possibly measure the performance on data that you do not know The solution
    to? This is the following realization is that given that you have a bunch of data,
    you were in charge. You get to control how much that your model sees. It works
    in the following way: You can hide data firms model. Let''s say you have a training
    data set which is a bunch of doubtless so X eyes are the features those are typically
    hide and national vector. It''s got more than one dimension for sure. And the
    why why eyes. Those are the labels for supervised learning. As you''ve seen before,
    it''s the same set up as we have in regression. And so you have this training
    data and now you choose that you only use some of those data to fit your model.
    You''re not going to use everything, you only use some of it the other part you
    hide from your model. And then you can use this hidden data to do validation from
    the point of you of your model. This hidden data is complete by unseen. In other
    words, we solve our problem of validation.'
  example_title: transcribed audio - lecture
- text: 'Transformer-based models have shown to be very useful for many NLP tasks.
    However, a major limitation of transformers-based models is its O(n^2)O(n 2) time
    & memory complexity (where nn is sequence length). Hence, it''s computationally
    very expensive to apply transformer-based models on long sequences n > 512n>512.
    Several recent papers, e.g. Longformer, Performer, Reformer, Clustered attention
    try to remedy this problem by approximating the full attention matrix. You can
    checkout 🤗''s recent blog post in case you are unfamiliar with these models.

    BigBird (introduced in paper) is one of such recent models to address this issue.
    BigBird relies on block sparse attention instead of normal attention (i.e. BERT''s
    attention) and can handle sequences up to a length of 4096 at a much lower computational
    cost compared to BERT. It has achieved SOTA on various tasks involving very long
    sequences such as long documents summarization, question-answering with long contexts.

    BigBird RoBERTa-like model is now available in 🤗Transformers. The goal of this
    post is to give the reader an in-depth understanding of big bird implementation
    & ease one''s life in using BigBird with 🤗Transformers. But, before going into
    more depth, it is important to remember that the BigBird''s attention is an approximation
    of BERT''s full attention and therefore does not strive to be better than BERT''s
    full attention, but rather to be more efficient. It simply allows to apply transformer-based
    models to much longer sequences since BERT''s quadratic memory requirement quickly
    becomes unbearable. Simply put, if we would have ∞ compute & ∞ time, BERT''s attention
    would be preferred over block sparse attention (which we are going to discuss
    in this post).

    If you wonder why we need more compute when working with longer sequences, this
    blog post is just right for you!

    Some of the main questions one might have when working with standard BERT-like
    attention include:

    Do all tokens really have to attend to all other tokens? Why not compute attention
    only over important tokens? How to decide what tokens are important? How to attend
    to just a few tokens in a very efficient way? In this blog post, we will try to
    answer those questions.

    What tokens should be attended to? We will give a practical example of how attention
    works by considering the sentence ''BigBird is now available in HuggingFace for
    extractive question answering''. In BERT-like attention, every word would simply
    attend to all other tokens.

    Let''s think about a sensible choice of key tokens that a queried token actually
    only should attend to by writing some pseudo-code. Will will assume that the token
    available is queried and build a sensible list of key tokens to attend to.

    >>> # let''s consider following sentence as an example >>> example = [''BigBird'',
    ''is'', ''now'', ''available'', ''in'', ''HuggingFace'', ''for'', ''extractive'',
    ''question'', ''answering'']

    >>> # further let''s assume, we''re trying to understand the representation of
    ''available'' i.e. >>> query_token = ''available'' >>> # We will initialize an
    empty `set` and fill up the tokens of our interest as we proceed in this section.
    >>> key_tokens = [] # => currently ''available'' token doesn''t have anything
    to attend Nearby tokens should be important because, in a sentence (sequence of
    words), the current word is highly dependent on neighboring past & future tokens.
    This intuition is the idea behind the concept of sliding attention.'
  example_title: bigbird blog intro
- text: 'To be fair, you have to have a very high IQ to understand Rick and Morty.
    The humour is extremely subtle, and without a solid grasp of theoretical physics
    most of the jokes will go over a typical viewer''s head. There''s also Rick''s
    nihilistic outlook, which is deftly woven into his characterisation- his personal
    philosophy draws heavily from Narodnaya Volya literature, for instance. The fans
    understand this stuff; they have the intellectual capacity to truly appreciate
    the depths of these jokes, to realise that they''re not just funny- they say something
    deep about LIFE. As a consequence people who dislike Rick & Morty truly ARE idiots-
    of course they wouldn''t appreciate, for instance, the humour in Rick''s existential
    catchphrase ''Wubba Lubba Dub Dub,'' which itself is a cryptic reference to Turgenev''s
    Russian epic Fathers and Sons. I''m smirking right now just imagining one of those
    addlepated simpletons scratching their heads in confusion as Dan Harmon''s genius
    wit unfolds itself on their television screens. What fools.. how I pity them.
    😂

    And yes, by the way, i DO have a Rick & Morty tattoo. And no, you cannot see it.
    It''s for the ladies'' eyes only- and even then they have to demonstrate that
    they''re within 5 IQ points of my own (preferably lower) beforehand. Nothin personnel
    kid 😎'
  example_title: Richard & Mortimer
parameters:
  max_length: 48
  min_length: 2
  no_repeat_ngram_size: 3
  encoder_no_repeat_ngram_size: 3
  early_stopping: true
  length_penalty: 0.1
  num_beams: 2
base_model: google/pegasus-x-large
model-index:
- name: pszemraj/pegasus-x-large-book-summary
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: test
    metrics:
    - type: rouge
      value: 33.1401
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjQ1NjY1OGVjYWEwMzBjMzk3ZmMyZDA0ZTcxOTdmZTUxNTc0OGYxYmY3MzJkMzFmYTVjNzU2ZTk4MzE0NWMzMSIsInZlcnNpb24iOjF9.PSHB6DMF6tkwSw5nsFE57a2ApRAy_tkS6ziKA6PSTWddEdaqfca4pfig6_olmRmcS4KxN6HHcsmioHzv4LJQBw
    - type: rouge
      value: 9.3095
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzk3MTA3NmY1OGE3MzFjZTJhYWYzNGU4NTUzMTgwM2Y1NWZjMmEyNDNmNmEzYmQzZThjOGExMjc2ZjAyZjMzZCIsInZlcnNpb24iOjF9.tfgp8p-WlkVrfducTSg4zs-byeZMCmdZw1aizPQHXm_qRAwGtKcuVkZcmza5Y3o3VqsAEmGzg5HQD1vnZvWIDA
    - type: rouge
      value: 24.8552
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTVmMTIwNDQwNTI4MmI2MmY1ODc1Mjk0NGQ5ZWE4ZTYzOGNkMjY2ZmJhMjg2MTZlNTdhYTA2ZDAxNTFjMjA2MSIsInZlcnNpb24iOjF9.9HLgy9842oIDm6ABb3L94R1P4zAqTI0QN8aP62xzIyDxUXTbWw68PEDufYLiBJbTgZ8ElopZ9I7aou2zCgXeAA
    - type: rouge
      value: 29.0391
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmNhYWJjYjdjMzMxMmE4ZTE4NGEzMDdmZDZjODI5ZWRjZWJmYTEyZGIzYWQ2NjM3YzQ4MjI4ZTM4MmU5MzRjZSIsInZlcnNpb24iOjF9.d2yoVdmxjVJnsgIYFiLuaBO5Krgw4Axl5yeOSTKrvHygrAxoqT1nl4anzQiyoR3PwYBXwBkwmgpJUfZ7RNXtDQ
    - type: loss
      value: 2.288182497024536
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzM5NGIwODMxOTA3MTY3ODc2ZDczYTNmMTMwM2QyZmNlZjFmZDJjMGY3NWNkMDEyYzA4OTA2ZDRiODY3Zjg4OCIsInZlcnNpb24iOjF9.8k9mC050OS7mQSR9oA8liDRDQvEx1VxmTXGLmDYJVYYtTh2HYJFGP8Vy_krocFRIYDxh-IHPEOOSr5NrLMWHBA
    - type: gen_len
      value: 45.2173
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWZhNzQ5OTQ5Yjg5YjhlOTZiZmJhZjZiODNmY2E2OTg4YTg4NWVhYzRkNzM2Mzk4NzdlMDgxM2M4NjY2YzhhYSIsInZlcnNpb24iOjF9.tDEEsPUclZDygAdGhNrBGrF24vR8ao08Nw7hmtUt5lmSZZZK_u-8rpz97QgVS6MCJdjFVnbYC4bkFnlQWI_FAA
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: launch/gov_report
      type: launch/gov_report
      config: plain_text
      split: test
    metrics:
    - type: rouge
      value: 39.7279
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTAxODk3OTUwMTIzODU3NzU2YzAzZjE2NTM3MzBjNDA0ZWRmZGU3NWUzNTg1YThhNDQ1NjQ5ZmM3OWI2YzBhNSIsInZlcnNpb24iOjF9.vnNKucBNt2-nIyODj9P2HeaWPX5AQR8L-DL8QzrO7kj58-vZnjT6hsAGmepRNzdZ1TLF-3j2J2plcNJ8lUO8Dg
    - type: rouge
      value: 10.8944
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjYzMmIxOTJmZjkxOGI5N2U0NTRmMmQwOGJhMzMxYWIzMWMzYzUwMDEyMDdiZDQ2YTUzOWU0OTViMTI2YTAwYiIsInZlcnNpb24iOjF9.De0PaAikWqfWpoIXTCYP-mSFu3PUATLX08Qq74OHXM8784heFVDX1E1sXlh_QbbKJbuMuZtTKM4qr7oLUizOAw
    - type: rouge
      value: 19.7018
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzI3MjQzOGQ3MGE3NDNkZTEyMWRkYjUyYTYzNDEwOWVjMGFmNTBiZjE4ZTBhMGYzMmI1Yzk0YjBmYmIzMWMxZSIsInZlcnNpb24iOjF9.FVikJ5Ma0gUgM-tpbomWXnC4jtmvhxqikPqCk84t4IbIdU0CIYGTQEONiz-VqI0fJeNrnTS6lxpBv7XxKoq3BQ
    - type: rouge
      value: 36.5634
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTI2OTVmNDZiZWE5ZjNkODIwZjJiNTU2ZjJjYjczODUwM2JiNDEzYmE3N2U5YWM5NzJjOWEzMmYzZjdlYWJmYyIsInZlcnNpb24iOjF9.poR4zcqRvdaierfWFdTa53Cv6ZbNbnRwyRTi9HukHF5AWAQgc6zpBLkwOYFYoWjuSH83ohWeMM3MoIdw3zypBw
    - type: loss
      value: 2.473011016845703
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDFmMjg3NWQ2YTMxMTc1OGZiYWYzNjg5NDY3MWE4MjY5ZDQxZDZhZGI1OTc5MzZkZGEzYmVlNWFiMzZjNDdhNCIsInZlcnNpb24iOjF9.05nKB3SmEfFKSduJqlleF4Fd2_IhwJS8eTOrnzZYCQQfLCfpJAZLhp3eLQCuBY4htd-FNrZftrThL66zVxyrCQ
    - type: gen_len
      value: 212.8243
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGNjMTg4ZDZlZjAxZGNhN2M0NWI0ZTA0OWEzNDkzNDAzOTJhODA2MmVkODI4YjYzN2FiOTU1ZDMwM2VlNWMyYyIsInZlcnNpb24iOjF9.WYx6XJFKokY2heoN-jpAMp1Z1gsyJus3zpktQgNd0FOYJxOUqW40A0kkHtd15y4dUhsbccLpuJGY1fNJgHOiDw
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: billsum
      type: billsum
      config: default
      split: test
    metrics:
    - type: rouge
      value: 42.1065
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDJhNDM2MWEwMjJlYjRmZTVkYzljODcwMzlmMGUxMDA4ZmRjNjM0NmY3ZWJlMmZjNGI3NDQ3NTQyOTQ3MjBkNSIsInZlcnNpb24iOjF9.l1MiZbXyFyXAcsfFChMrTvSaBhzBR6AuDnBuII8zY3Csz3ShWK0vo09MkQdZ1epe8PKWV9wwUBuJyKk3wL7MDw
    - type: rouge
      value: 15.4079
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTY3NDBkYTVkNjdhY2I0ZmY0NTA4YzVkMGE5YWE5ODdjOGE1MDhkOTJhOWY3NmI2ZWI1MGU2MGI1NDRlYjI3MSIsInZlcnNpb24iOjF9.VN-5eK2SzFDCJnFTHHu7XCU_lynaxW_JEDc3llmcNo_ffDgRmISHHGaqV7fPFymBBMXpPly7XblO_sukyqj1Cg
    - type: rouge
      value: 24.8814
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDYyNGZmNDY3MTY4YzI4ZjZhODE0NGIyN2ZkOGEyYzM3MWZjM2QzZTg5ZjNmZmYzZDE5NzhiZDQ4OGM1YjNiMyIsInZlcnNpb24iOjF9.L73M1M5XdMQkf8zSdfLN0MUrxtO0r6UiLjoOkHfrIGbWNsNJ8tU5lciYFNIhJrICUL8LchCsFqR9LAClKS4bCg
    - type: rouge
      value: 36.0375
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTBlMTQ5OTQxNTA3ZmFiMGYyZWQ0MGM0ODY2YWI3MzgyNjkwNzQyM2FmNGRjMzc3MjJmZDZkOWY4M2RhZTg2MSIsInZlcnNpb24iOjF9.IiMSSVahBgH8n34bGCC_DDGpujDXQbIvGhlcpVV2EBVQLLWUqcCy5WwBdbRrxPC-asBRCNERQxj8Uii4FvPsDQ
    - type: loss
      value: 1.9130958318710327
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTg2NTMxZDE3MDg3MDFkMTYxNjY1OTc5YjQ4ODcyMGUxMTFiZjJiNDgyYWZhN2NjZmE1MDQ1NTRmZGY0NjQzZSIsInZlcnNpb24iOjF9.kADUBMO8i6-oGDDt1cOiGMrGcMkF_Qc1jSpS2NSFyksDRusQa_YuuShefF4DuHVEr3CS0hNjjRH9_JBeX9ZQDg
    - type: gen_len
      value: 179.2184
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjM4NGNiMTY3YzZjMzg4MTRiMDdiZDFiMzA1ZDIyMDM2MDk1OWRhYWQzN2UxZDNlODIxOWVhY2JlYjk4Mjk5YyIsInZlcnNpb24iOjF9.nU8ImMNWgjg9BKjUBJQLFaJOBq3kyIne8ldlpL0OV0e4888wOntIAcJP0dCCYfRSLVmZuXQ1M8cpDuTf50hNCw
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: kmfoda/booksum
      type: kmfoda/booksum
      config: kmfoda--booksum
      split: test
    metrics:
    - type: rouge
      value: 35.2154
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWQ5MGMzNDc4MDBiNmRiNDY5ZDM4N2QzYTJlYTNiYTcwNDBlMzdlM2I4N2VmM2ZjMmQ3NGU3OTRlMTMzMTg3NyIsInZlcnNpb24iOjF9.E55gu7HvMwc4HejF3YOD6yqQJj7_6GCoCMWm78sY5_w2glR-oM98tu9IsG27VaPva7UklxsspzT2DIVaVKY0CQ
    - type: rouge
      value: 6.8702
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjFhN2JlYzlmMGZmYzkwYjBlNjY4YzhlYzNmMTdmZWYyYmU3NWI0ZTRkMTgxNmRiM2EyZWMyMWFjY2JkNzg1MCIsInZlcnNpb24iOjF9.I9BoHbGt8LLNtLAssIXm9tQ4lHqFCMt0zJS_zTezzxGRMS5On71c3jnlzrDtwEm6wjmZEwYIJK8qqJh-Qa5YAA
    - type: rouge
      value: 17.6693
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGZlZjcwOTZjMmNjZWFkM2M5Zjg1OTgzMzcxOTM2Y2RkMzY4NGU2NDE2MTVjMjcyMWIwNWI4ODc0YTY3YTA2MSIsInZlcnNpb24iOjF9.Ou1C6U6PrOtXPxlk9PMucdJ_vlnVnSk94QrLJL4b_g2pcY3D80Xrw09iz4BTOPzZ2UTNBLyn8YdLY3m2vHpiAQ
    - type: rouge
      value: 32.8365
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmIzMGQ5MzQ1MjI4MTU0ZGZkZTRhODllNWQyOTQ4ZjA5YWE4ZTJjMzQ2ZWQzOGFiMWUzZDMxOTU5NzkxYjliZiIsInZlcnNpb24iOjF9.2mYURQZYo7e3AY0tfkpqFMNhoHvrysvBXza-XYYrX_xLpruMU9Gzrwc3jvpi2wtp4eeyhzIiZJvH0O6la6zxCg
    - type: loss
      value: 2.9878039360046387
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGU0ODBmN2I3OGFkNTFiM2I3YWQyNmUzNzUwYzEwNzczZWEwZjIxYTAwZDE2ZTIwMGE3ZGNmMDQzNTFmNjEwYyIsInZlcnNpb24iOjF9.0IKWIImKTXqysQUb2IMPk2eeHlOcBjndiPcU42nfFBMhRTqeXdBqOCP6cidlho7pVN4hsC-77ArJ9pZlbTFuBg
    - type: gen_len
      value: 200.6785
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDUzYTE3MmIxZGM3MWI1MjNhMTU3MTdkMjJjNjY5Y2UzYTdjYWRiY2I4MmUxMDY4NTA5NWZjYWU0NzliODdkYiIsInZlcnNpb24iOjF9.BqmCaWzbCMNUied6zNO744Dl-0LC47FCIv-l8kDjkhSkwQcb_hi93VYts5PTsrFY_MmM8j7AsY1PiFr6nNFMBQ
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: big_patent
      type: big_patent
      config: y
      split: test
    metrics:
    - type: rouge
      value: 37.376
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWI4ZjMxODcxMThiMzE3NjQ3Zjg0NzhmZjlhY2ZmYjQwMGY5ZjlkZGY1MzZmY2M5YTU4NmY1Y2NhZDA3YWFkOCIsInZlcnNpb24iOjF9.sYh4IynXgOpVetYYSWUp0v5QZWvXC1x7_uJR0LZUxaeYKEc4yfICNmDOPzNzoroaV4ELeOaPjHQpYVm-lpAHBA
    - type: rouge
      value: 11.4432
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTZkOGIyYzU3YTQ5ZTFmMDU3MjQ5ZWM2NGQ1MzgwMDYyZDkxN2Q2YjgyZTkzMTEyYjczMGJiYmNkZmU5MTQ3NSIsInZlcnNpb24iOjF9.Qk38acpjPjU64Z1nXEuqMXjKZrGvdC9oY586EjuCPeEAJCSzKimp8FsB-1QrjMH73q6rN2CdumJUxih6HF-KAA
    - type: rouge
      value: 22.2754
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzlmOTUxYmEzYzYyYmVjNGZlNzNiZWIwZmQ5OWVlY2U3NTBiZDExYWUwODQ0Y2ZjMmQyMTNmMTlmNjdmZWUwNCIsInZlcnNpb24iOjF9.bUVhxaepySyaityby71j6h4YO_l4x8OSeZoblagwUMYGXRc0Ej286QzEtZFeRGygMJ5sjUN_loWCtOmAnHY2BA
    - type: rouge
      value: 32.5087
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDEyNjM5NjAzYTNjN2MwZTY4MWY2Y2U5YWUyM2Y1YjAyNjBhZTM0YTAyZjM5N2M1ZDkxOWUxNzE2OWZkYTBmMSIsInZlcnNpb24iOjF9.QfMHkcoAR3xqzsgL1xjHk3Lui1xhE12pJKvYujQ_h5o6PBXT79dsENsrqDGGBjiKdTKNwWqADgaviy1VrWMDCQ
    - type: loss
      value: 2.9867310523986816
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTUzM2Q5MmE5MzU4YmFlMjFiMmUzZGU2NDAzMTQ1Y2NjZDVlYWI3NGE5MjM0NmMxMjdiOWI3MTU0NDk3NmNkZiIsInZlcnNpb24iOjF9.VoQqu6ZU3AR_cji82UkpvbLnTmZ17fZmR2E4DeonjCyTZpyyfvUsQ2nbKDovQf34DBkYXENk42EUsUF1mBZNBg
    - type: gen_len
      value: 172.7776
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTEzNTMyMDY1N2Q5ZTMxNjNlMTI0Nzk5ZDc1ZWQ5Y2IwZWM0NWNhNWY2MTk3YTRkYzUwMTI4NjZiOWVhOGQwYSIsInZlcnNpb24iOjF9.-Rek2VFmGqIEgqeFoxU_0aCWdFbGYi9BV5c7x-izm9_4vtZdYQ4ITXm4T8C3UlpOax60veJQt2Uax5vyiFc9Ag
---

# pszemraj/pegasus-x-large-book-summary


<a href="https://colab.research.google.com/gist/pszemraj/6c326c0649233ab017d63adc36958d1a/pegasus-x-large-booksum-demo.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Get SparkNotes-esque summaries of arbitrary text! Due to the model size, it's recommended to try it out in Colab (linked above) as the API textbox may time out.

This model is a fine-tuned version of [google/pegasus-x-large](https://huggingface.co/google/pegasus-x-large) on the `kmfoda/booksum` dataset for approx eight epochs.


## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

#### Epochs 1-4

TODO

#### Epochs 5 & 6
The following hyperparameters were used during training:

- learning_rate: 6e-05
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 32
- total_train_batch_size: 128
- optimizer: _ADAN_ using lucidrains' `adan-pytorch` with default betas
- lr_scheduler_type: constant_with_warmup
- data type: TF32
- num_epochs: 2

#### Epochs 7 & 8

- epochs 5 & 6 were trained with 12288 tokens input
- this fixes that with 2 epochs at 16384 tokens input

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: _ADAN_ using lucidrains' `adan-pytorch` with default betas
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 2

### Framework versions

- Transformers 4.22.0
- Pytorch 1.11.0a0+17540c5
- Datasets 2.4.0
- Tokenizers 0.12.1