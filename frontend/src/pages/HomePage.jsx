import React from "react";
import Layout from "../components/Layout/Layout";
import Banner from "../components/Home/Banner";
import PromoVideo from "../components/Home/Video";
import WorldWide from "../components/Home/WorldWide";

function HomePage() {
  return (
    <Layout>
      <Banner />
      <PromoVideo />
      <WorldWide />
    </Layout>
  );
}

export default HomePage;
