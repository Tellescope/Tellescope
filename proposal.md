![Tellescope Logo](https://raw.githubusercontent.com/davdhng/tellescope/master/assets/logo.png)


# Tellescope: A Messaging Interaction Model for Product Discovery

Kathryn Britt, David Huang, Jacob Hutchison, Jack Oh, James Oh

02 March 2018



## 1. Abstract
Shoppers often have a hard time finding products in stores. Although e-commerce has streamlined the shopping process, customers will still shop at physical brick-and-mortar stores for immediacy and impulse reasons, or to inspect and assess product quality. Conventional retail and grocery stores deliberately structure their aisles to maximize the amount of time a customer spends inside the store, which discourages the immediacy/impulse shoppers when a particular item cannot be located. Tellescope is our proposed solution that seeks to provide a convenient experience for immediacy/impulse shoppers while remaining unobtrusive for regular customers. 

Tellescope consists of  a facial sentiment analysis system based on human shopping patterns and a mobile chatbot to facilitate brand interaction while remaining fast and intuitive. The interaction model and sentiment analysis system are designed in this project. 

## 2. Background
Although smartphones have become universal amongst shoppers, most stores neglect to effectively use these to create more personalized customer experiences at their physical locations. Current efforts at personalization remain online through e-commerce and other rewards programs. Customers expect similar experiences in both online and physical stores, but these experiences remain detached, because stores are plagued by:

1.	Frequent changes in layout and stocking areas
2.	Poor employee interactions with customers
3.	Limited engagement with customers in brick-and-mortar locations

A new in-store experience is needed to bring the benefits of a store’s mobile and online experiences to the physical world. This experience must:

1.	Be personalized to the needs of the customer
2.	Be as fast and effortless as possible
3.	Facilitate engagement between brands and customers

Current solutions, such as Target’s mobile application, cater to immediacy/impulse customers by allowing them to search for items and find their location and availability inside their chosen store. A digitized map of the store is created for reference. However, the Target app is able to display only the location of the item, and cannot show the user’s location in relation to the item’s. It is also worth mentioning that other apps have employed augmented reality to assist in product location, yet this method is not widely adopted, because it requires an augmented-reality-enabled smartphone. This project proposes a novel physical and mobile shopping experience that provides a fast, personalized solution to locate in-store items through computer vision and a messaging interaction model.

## 3. Tellescope Item Location System
Tellescope is a proposed system for product location in physical brick-and-mortar retail and grocery stores. The Tellescope system consists of two fundamental components: 

1.	In-Store Experience
a.	A camera-centered sentiment analysis solution to facilitate a more organic assistance experience.
b.	Bluetooth low energy beacons will be placed along the aisles of participating stores for convenient access to a chatbot.
2.	Conversational AI
a.	A visibly frustrated or confused customer can interact with a mobile chatbot through a web browser to ask for product availability, location, or alert an in-store employee.

The increased demand for improved in-store experiences will likely offset the installed cost and system maintenance.  

### 3.1. User Experience
Before introducing the next section concerning customer sentiment analysis, it is necessary to understand human shopping habits. A common algorithm for shopping in an unfamiliar retail or grocery store is to first browse along the perimeter of the store and lastly enter the aisles at the center of the store. Not only does this equip the shoppers with a basic understanding of the store layout, but they are also able to read signs that can detail aisle contents. 

However, a specific item can be particularly difficult to find, especially in a large store. Customers usually prefer to solve their problems initially unaided, and would only ask for help if they are unable to solve the problem themselves. Therefore, it is illogical to assume that  customers will install an app, scan a QR code, and type in an item when they are first entering a store. It can be concluded that customers would most likely require a product location solution when they are frustrated and wandering through the middle aisles of the store—not when they first enter. 

The goal of Tellescope is to be ubiquitous, yet unobtrusive. A frustrated customer should be able to instantly access the Tellescope system intuitively, without needing to consciously download an app. Interacting with Tellescope should be as simple as unlocking your phone.

### 3.2. Customer Sentiment Analysis
To provide the shopper with information, the Tellescope system must first be able to detect if the shopper is having trouble finding a product, in the same way a store associate would scan for shoppers who appear to need assistance. Multiple low-profile cameras will be placed around the store and along the aisles. A face detection algorithm would be continuously running on each camera to detect emotions and analyze positive or negative sentiments. The algorithm will analyze a video feed of the customer and output a confidence score for the six universally recognized facial expressions—joy, surprise, sadness, anger, disgust, and fear. A customer exhibiting a happy or neutral facial expression does not trigger the system. 

If a customer exhibits a high confidence score for emotions with a negative sentiment, such as anger or disgust, the Tellescope system will trigger a nearby bluetooth beacon (also placed throughout the store and along the aisles), which will send a notification to the nearby customer’s bluetooth-enabled smartphone. This nearby notification does not require an app installation, but will instead open a link to an HTTPS URL when the customer interacts with the notification. This allows the customer to begin interacting with a custom store chatbot.

### 3.3. Chatbot
Interacting with a conversational AI, the customer can avoid searching the store for an available employee, but would also improve store productivity by reducing employee distractions. The conversational interface would be built in the Elixir programming language, and can be interacted with through a customer’s web browser. Using natural language processing, the chatbot would interpret questions, such as those asking for the location or availability of a particular product. A simple menu-based interface may also be implemented to more effectively guide the user.  The chatbot is connected to a database consisting of the retail or grocery store’s current inventory and their locations and will query it as needed. If a query matches an item in the inventory, the Tellescope chatbot will tell the user the section and aisle number of the specified product, as well as its relative location. For example, the chatbot will respond to “where is peanut butter” with “Groceries: A67, near the front of the store to the right”.   

### 3.4. Privacy 
Some people might not be comfortable being recorded while they are shopping and feel it is a violation of their privacy. Stores should notify customers when they enter that they are using Tellescope and recording their faces for an enhanced shopping experience. Customers should also be informed that the data being collected is purely numerical and does not contain any personally-identifiable information.

## 4. Conclusions
This document has detailed an indoor navigation system named Tellescope. Catering to the immediacy/impulse customer, Tellescope enables an intuitive, frictionless method for finding products without the need to download an app. A conversational interface facilitates brand engagement with customers while providing information personalized to the needs of the customer.






