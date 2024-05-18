if mode == "train":
    # Train the model.
    model.train()
elif mode == "eval":
    # Evaluate the model.
    model.eval()
elif mode == "predict":
    # Predict using the model.
    model.predict()
else:
    raise ValueError("Invalid mode: {}".format(mode))
