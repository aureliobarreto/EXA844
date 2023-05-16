"use client"; 

import React, { useState } from 'react';
import { ChakraProvider } from '@chakra-ui/react';
import styles from './page.module.css';
import { FilterableMessagesTable } from './components';

function formatarData(dataString) {
  const date = new Date(dataString);
  const dia = date.getDate().toString().padStart(2, '0');
  const mes = (date.getMonth() + 1).toString().padStart(2, '0');
  const ano = date.getFullYear().toString().substr(-2);
  const hora = date.getHours().toString().padStart(2, '0');
  const minutos = date.getMinutes().toString().padStart(2, '0');
  const segundos = date.getSeconds().toString().padStart(2, '0');

  return `${dia}/${mes}/${ano} ${hora}:${minutos}:${segundos}`;
}

export default function Home() {
  const [blogMessages, setBlogMessages] = useState([]);

  fetch('https://script.google.com/macros/s/AKfycbzBn3sALe1rYjz7Ze-Ik7q9TEVP0I2V3XX7GNcecWP8NvCzGt4yO_RT1OlQp09TE9cU/exec')
    .then(response => response.json())
    .then(data => {
      const messagesFormatted = data.map(array => {
        const [message, author, dateString] = array;
        const formattedDate = formatarData(dateString);
        return [message, author, formattedDate];
      });
      setBlogMessages(messagesFormatted);
    });

  return (
    <ChakraProvider>
      <main className={styles.main}>
        <FilterableMessagesTable messages={blogMessages} />
      </main>
    </ChakraProvider>
  );
}

