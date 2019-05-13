# Welcome!

I'm sure you're here to check on the network latencies-- let me show you around! I know you might be having to set this up at an inconvenient time (2am!), so I just wanted to list out these straightforward steps so you might be able to better detect what issue there might be (if there is one) through the different request latencies we've been tracking!

Let's get started!

More formally: The user is a fellow developer that has to check on different issues with our servers, and in order to do so, he/she may need to take a look at the latencies of different requests for the past hour, to see exactly when things stopped working, and by how significant of an amount.

## Project setup

To begin, you'll need to [clone this repo locally](https://help.github.com/en/articles/cloning-a-repository), and then run the following the command in terminal/command prompt!

```
npm install
```

This will install all the necessary packages for us to be able to render the dashboard appropriately!

### Compling and running the files

Now that we've got the packages set up, we'll be able to run the files locally now, with the following command:

```
npm run serve
```

When done, your terminal/command prompt should list something like the following: `Local: http://localhost:8080/`. You can copy and paste that URL into any web browser, and be able to see the dashboard of the request latencies over the past hour, at 5 minute intervals! Enjoy!
