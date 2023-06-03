<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">15</span><span style=" color:#00ff00;">]:</span> runfile('E:/Face Recognition/FaceReconition.py', wdir='E:/Face Recognition')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Model: &quot;model_6&quot;</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> Layer (type)                Output Shape              Param #   </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> input_7 (InputLayer)        [(None, 224, 224, 3)]     0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv1 (Conv2D)       (None, 224, 224, 64)      1792      </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv2 (Conv2D)       (None, 224, 224, 64)      36928     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_pool (MaxPooling2D)  (None, 112, 112, 64)      0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv1 (Conv2D)       (None, 112, 112, 128)     73856     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv2 (Conv2D)       (None, 112, 112, 128)     147584    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_pool (MaxPooling2D)  (None, 56, 56, 128)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv1 (Conv2D)       (None, 56, 56, 256)       295168    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv2 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv3 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_pool (MaxPooling2D)  (None, 28, 28, 256)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv1 (Conv2D)       (None, 28, 28, 512)       1180160   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv2 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv3 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_pool (MaxPooling2D)  (None, 14, 14, 512)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv1 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv2 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv3 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> flatten_6 (Flatten)         (None, 25088)             0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> dense_6 (Dense)             (None, 4)                 100356    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Total params: 14,815,044</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Trainable params: 100,356</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Non-trainable params: 14,714,688</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 373 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 208 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">e:\face recognition\facereconition.py:83: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  r = model.fit_generator(</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 1/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 63s 5s/step - loss: 0.5653 - accuracy: 0.8257 - val_loss: 1.0307 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 2/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 62s 5s/step - loss: 0.0180 - accuracy: 0.9973 - val_loss: 2.7195 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 3/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 60s 5s/step - loss: 0.0051 - accuracy: 1.0000 - val_loss: 3.0271 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 4/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 60s 5s/step - loss: 0.0047 - accuracy: 0.9973 - val_loss: 3.2039 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 5/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 63s 5s/step - loss: 0.0051 - accuracy: 0.9973 - val_loss: 3.2639 - val_accuracy: 0.7452</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img238856016232453.png"></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img238937620611077.png"></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;Figure size 432x288 with 0 Axes&gt;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">16</span><span style=" color:#00ff00;">]:</span> runfile('E:/Face Recognition/Vgg16modeltrain.py', wdir='E:/Face Recognition')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Model: &quot;model_7&quot;</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> Layer (type)                Output Shape              Param #   </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> input_8 (InputLayer)        [(None, 224, 224, 3)]     0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv1 (Conv2D)       (None, 224, 224, 64)      1792      </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv2 (Conv2D)       (None, 224, 224, 64)      36928     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_pool (MaxPooling2D)  (None, 112, 112, 64)      0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv1 (Conv2D)       (None, 112, 112, 128)     73856     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv2 (Conv2D)       (None, 112, 112, 128)     147584    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_pool (MaxPooling2D)  (None, 56, 56, 128)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv1 (Conv2D)       (None, 56, 56, 256)       295168    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv2 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv3 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv4 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_pool (MaxPooling2D)  (None, 28, 28, 256)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv1 (Conv2D)       (None, 28, 28, 512)       1180160   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv2 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv3 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv4 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_pool (MaxPooling2D)  (None, 14, 14, 512)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv1 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv2 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv3 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv4 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> flatten_7 (Flatten)         (None, 25088)             0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> dense_7 (Dense)             (None, 4)                 100356    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Total params: 20,124,740</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Trainable params: 100,356</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Non-trainable params: 20,024,384</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 373 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 208 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">e:\face recognition\vgg16modeltrain.py:83: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  r = model.fit_generator(</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 1/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 80s 7s/step - loss: 0.8314 - accuracy: 0.7426 - val_loss: 1.8887 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 2/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 80s 7s/step - loss: 0.0446 - accuracy: 0.9786 - val_loss: 1.8492 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 3/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 81s 7s/step - loss: 0.0190 - accuracy: 0.9973 - val_loss: 1.9049 - val_accuracy: 0.7548</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 4/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 83s 7s/step - loss: 0.0047 - accuracy: 0.9973 - val_loss: 2.1882 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 5/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 84s 7s/step - loss: 0.0022 - accuracy: 1.0000 - val_loss: 2.4028 - val_accuracy: 0.7452</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img304298432921605.png"></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">~\.conda\envs\MajorProject\lib\site-packages\spyder_kernels\py3compat.py:356</span> in <span style=" color:#9400d3;">compat_exec</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    exec(code, globals, locals)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">e:\face recognition\vgg16modeltrain.py:98</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    plt.plot(r.history['acc'], label='train acc')</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00ffff;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">KeyError:</span> 'acc'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;Figure size 432x288 with 0 Axes&gt;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">17</span><span style=" color:#00ff00;">]:</span> runfile('E:/Face Recognition/Vgg19modeltrain.py', wdir='E:/Face Recognition')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Model: &quot;model_8&quot;</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> Layer (type)                Output Shape              Param #   </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> input_9 (InputLayer)        [(None, 224, 224, 3)]     0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv1 (Conv2D)       (None, 224, 224, 64)      1792      </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv2 (Conv2D)       (None, 224, 224, 64)      36928     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_pool (MaxPooling2D)  (None, 112, 112, 64)      0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv1 (Conv2D)       (None, 112, 112, 128)     73856     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv2 (Conv2D)       (None, 112, 112, 128)     147584    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_pool (MaxPooling2D)  (None, 56, 56, 128)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv1 (Conv2D)       (None, 56, 56, 256)       295168    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv2 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv3 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv4 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_pool (MaxPooling2D)  (None, 28, 28, 256)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv1 (Conv2D)       (None, 28, 28, 512)       1180160   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv2 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv3 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv4 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_pool (MaxPooling2D)  (None, 14, 14, 512)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv1 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv2 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv3 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv4 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> flatten_8 (Flatten)         (None, 25088)             0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> dense_8 (Dense)             (None, 4)                 100356    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Total params: 20,124,740</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Trainable params: 100,356</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Non-trainable params: 20,024,384</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 373 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 208 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">e:\face recognition\vgg19modeltrain.py:83: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  r = model.fit_generator(</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 1/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 80s 7s/step - loss: 0.6200 - accuracy: 0.8177 - val_loss: 2.0229 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 2/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 77s 7s/step - loss: 0.0308 - accuracy: 0.9893 - val_loss: 2.5578 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 3/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 75s 6s/step - loss: 0.0170 - accuracy: 0.9946 - val_loss: 2.1785 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 4/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 76s 6s/step - loss: 0.0046 - accuracy: 0.9973 - val_loss: 2.3377 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 5/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 76s 7s/step - loss: 0.0017 - accuracy: 1.0000 - val_loss: 2.7429 - val_accuracy: 0.7452</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img328479098798085.png"></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img328573588078597.png"></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;Figure size 432x288 with 0 Axes&gt;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">18</span><span style=" color:#00ff00;">]:</span> runfile('E:/Face Recognition/Vgg16modeltrain.py', wdir='E:/Face Recognition')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Model: &quot;model_9&quot;</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> Layer (type)                Output Shape              Param #   </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> input_10 (InputLayer)       [(None, 224, 224, 3)]     0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv1 (Conv2D)       (None, 224, 224, 64)      1792      </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_conv2 (Conv2D)       (None, 224, 224, 64)      36928     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block1_pool (MaxPooling2D)  (None, 112, 112, 64)      0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv1 (Conv2D)       (None, 112, 112, 128)     73856     </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_conv2 (Conv2D)       (None, 112, 112, 128)     147584    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block2_pool (MaxPooling2D)  (None, 56, 56, 128)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv1 (Conv2D)       (None, 56, 56, 256)       295168    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv2 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_conv3 (Conv2D)       (None, 56, 56, 256)       590080    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block3_pool (MaxPooling2D)  (None, 28, 28, 256)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv1 (Conv2D)       (None, 28, 28, 512)       1180160   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv2 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_conv3 (Conv2D)       (None, 28, 28, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block4_pool (MaxPooling2D)  (None, 14, 14, 512)       0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv1 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv2 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_conv3 (Conv2D)       (None, 14, 14, 512)       2359808   </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> flatten_9 (Flatten)         (None, 25088)             0         </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> dense_9 (Dense)             (None, 4)                 100356    </p>
<br/>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">=================================================================</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Total params: 14,815,044</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Trainable params: 100,356</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Non-trainable params: 14,714,688</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">_________________________________________________________________</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 373 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Found 208 images belonging to 4 classes.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">e:\face recognition\vgg16modeltrain.py:83: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  r = model.fit_generator(</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 1/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 63s 5s/step - loss: 0.5245 - accuracy: 0.8472 - val_loss: 2.8288 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 2/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 66s 6s/step - loss: 0.0087 - accuracy: 0.9973 - val_loss: 2.6649 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 3/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 61s 5s/step - loss: 0.0094 - accuracy: 0.9973 - val_loss: 2.8122 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 4/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 61s 5s/step - loss: 0.0024 - accuracy: 1.0000 - val_loss: 3.0155 - val_accuracy: 0.7452</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Epoch 5/5</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">12/12 [==============================] - 69s 6s/step - loss: 0.0056 - accuracy: 0.9973 - val_loss: 3.1611 - val_accuracy: 0.7452</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img399633821990917.png"></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="FaceRecognition_files/qt_img399706836434949.png"></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;Figure size 432x288 with 0 Axes&gt;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">19</span><span style=" color:#00ff00;">]:</span> runfile('E:/Face Recognition/untitled0.py', wdir='E:/Face Recognition')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">e:\face recognition\untitled0.py:30: SyntaxWarning: &quot;is&quot; with a literal. Did you mean &quot;==&quot;?</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  if faces is ():</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">~\.conda\envs\MajorProject\lib\site-packages\spyder_kernels\py3compat.py:356</span> in <span style=" color:#9400d3;">compat_exec</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    exec(code, globals, locals)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">e:\face recognition\untitled0.py:18</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    model = load_model('facefeatures_new_model_finalVGG19.h5')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">~\.conda\envs\MajorProject\lib\site-packages\keras\utils\traceback_utils.py:70</span> in <span style=" color:#9400d3;">error_handler</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    raise e.with_traceback(filtered_tb) from None</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">~\.conda\envs\MajorProject\lib\site-packages\keras\saving\save.py:226</span><span style=" color:#00ffff;"> in </span><span style=" color:#ff00ff;">load_model</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    raise IOError(</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00ffff;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">OSError:</span> No file or directory found at facefeatures_new_model_finalVGG19.h5</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">20</span><span style=" color:#00ff00;">]:</span> </p></body></html>