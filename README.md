# NLP-Project
## Phase 1
- We used the cartography code from the AllenAI repo
- Generated confidence and variability values for each data point while training the Roberta large model.
- Plotted the datamap
## Phase 2
- For every dataset we had performed the below steps.
- We sampled 5000 rows from the train file(train.csv) for all the datasets.
- Then we trained the bert-uncased model with train.csv as the training and validation file for 5 epochs with the below command. It will generate 5 files containing the predicted probabilities for each class for a respective row.
  - python3 training.py --model_name_or_path bert-base-uncased --num_labels 4 --hidden_dropout_prob 0.15 --max_input_seq_length 128 --output_dir ./  --predictions_file predictions.csv --TRAIN_FILE train.csv  --DEV_FILE train.csv --train_batch_size 16 --eval_batch_size 16 --max_train_samples -1 --num_train_epochs 5 --gradient_accumulation_steps 1 --seed 42 --save_top_k -1 --learning_rate 5e-05 --write_dev_predictions
- We then generated confidence scores and difficulty scores for each of the 5000 rows. Using those we plotted the datamaps.
- We need to train the bert-uncased delivery with train_5000 and dev to compare the performance of the model trained on selected data.
- After plotting the datamaps, we then performed data selection. Initially, we generated 3 datasets: easy.csv(Only contains points in the easy region), hard.csv(Only contains points in the hard region), and ambi.csv(Only contains points in the ambiguous region). Then we trained the bert-uncased model using each as the training file and dev.csv for the validation.
- After this we experimented to perform data selection with varying ratios of samples from easy, hard, and ambiguous regions.
