# detect_and_segment_solar_panels_in_satellite_photos



**This project was completed in several steps as outlined below:**

1-Dataset Generation:
2-Labeling roofs and solar panels.
3-Fine-tuning YOLOv8 and Fast R-CNN:
    Utilizing transfer learning techniques to fine-tune the YOLOv8 and Fast R-CNN models on the generated dataset.
Evaluation of Performance:
     Assessing the performance of the fine-tuned models, which includes measuring their accuracy, precision, recall, and other relevant evaluation metrics.


box_loss — bounding box regression loss (Mean Squared Error).
obj_loss — the confidence of object presence is the objectness loss.
cls_loss — the classification loss (Cross Entropy).

**for the see the result of model you can run jupyter notbook with name 4_final_step_test_the_models.ipynb**
**or you can chek the folder name figure_results**


the folder output contain the result of detectron faster_rcnn results
the folder runs contain the result of YOLOv8 results
-----------------------------------------------------------------------
Fast R-CNN:
-----------------------------------------------------------------------
"fast_rcnn/cls_accuracy": 0.8984375, 
"fast_rcnn/false_negative": 0.2300646551724138, 
"fast_rcnn/fg_cls_accuracy": 0.7543103448275862, 
"iteration": 499, 
"loss_box_reg": 0.3961748331785202, 
"loss_cls": 0.2448759526014328,
"loss_rpn_cls": 0.022156368009746075, 
"loss_rpn_loc": 0.019169245846569538, 
"lr": 0.000998002,
"roi_head/num_bg_samples": 48.0,
"roi_head/num_fg_samples": 16.0,
"rpn/num_neg_anchors": 235.625, 
"rpn/num_pos_anchors": 20.375, 
"time": 2.324711917999821
"total_loss": 0.7244632872752845
"bbox/AP": 31.025621141959515,
"bbox/AP-panel": 23.276776283859615,
"bbox/AP-roof": 38.77446600005941, 
"bbox/AP-roof-panel": NaN,
"bbox/AP50": 52.37187493136375, 
"bbox/AP75": 31.544120151896593, 
"bbox/APl": 38.266933272018974,
"bbox/APm": 27.348813899395747,
"bbox/APs": 7.722103522445104, 
"iteration": 500
-----------------------------------------------------------------------
YOLOv8
-----------------------------------------------------------------------
epoch:  133,   
train/box_loss:  0.42573, 
train/cls_loss:   0.3037,
train/dfl_loss:  0.87102, 
metrics/precision(B): 0.72394,  
metrics/recall(B):0.58181,  
metrics/mAP50(B):0.62464, 
metrics/mAP50-95(B):  0.43602,
val/box_loss:1.0356,
val/cls_loss:1.3467,            
val/dfl_loss:1.3913, 
lr/pg0: 0.003466,         
lr/pg1:   0.003466   
lr/pg2:0.003466
-----------------------------------------------------------------------

**steps of project**

In the first step, I searched the object detection context and found two state-of-the-art models: YOLO and Fast R-CNN. After evaluating them, I decided to try these two models. 

I also searched for a suitable dataset, but unfortunately, I couldn't find any appropriate open-source dataset. beacuse data is the fuel of AI, I decided to create a high-quality dataset myself.
(CNNs are quite powerful but without data, there is not much you can do.)

I attempted to use satellite images like Sentinel-2 and Landsat, but due to their low resolution, I decided to use Google Maps to collect the dataset. 
In this step, I used Google Earth Engine and Python to capture images from regions that contained roofs and solar panels.

My dataset encountered some challenges. Firstly, due to limitations in collecting a sufficient number of solar panel images compared to roofs, the final dataset ended up being unbalanced. However, given the time constraints, it was the best I could achieve.
Another issue with my dataset is the geographical bias. The majority of the images were collected from America and Europe. As a result, the model was trained on data that may not accurately represent the diverse appearances of roofs in Asia or Africa, due to variations in architecture and weather conditions. It is important to acknowledge these limitations when interpreting the results of the trained model.

In the next step, I had to annotate and label the roofs and solar panels in the images. To simplify this task, I discovered an model called SAM (Segment Everything by facebook). Additionally, I found an online platform called roboflow.com that leveraged the SAM algorithm, making the annotation process much easier. So I created two datasets: one in YOLO format for  traning YOLOv8 model and another in COCO dataset format for training the Fast R-CNN model using Detectron2.
Next, I performed fine-tuning of a pre-trained model using my created dataset and evaluated the results. Due to resource limitations, I utilized Google Colab to train the model on a GPU, which restricted my ability to extensively modify hyperparameters or increase the number of training epochs.
In the last step, I put everything together and created a notebook to test the fine-tuned model. This allowed me to compare the results obtained by these two models. In my evaluation, I found that Detectron2 provided a combination of speed and accuracy, earning a perfect score of 20/20