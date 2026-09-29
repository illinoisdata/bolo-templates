---
datasets:
- gerbejon/WebClasSeg25-MC
base_model:
- nvidia/mit-b0
---

**Task Description**

The model is designed to create segmentations of screenshots of websites to assess their digital maturity. This is achieved by classifying different segments of the webpage into predefined maturity classes. The maturity classification (MC) is based on a maturity index developed from existing approaches in political maturity indexes of websites. The segments or content within these segments are labeled with the following maturity classes:
Maturity Classes

- *Information 1.0 (0)*
    Description: Information with action from the user, such as downloads for information (e.g., PDFs           or videos). This does not include forms.
Example: A list of downloadable reports in PDF format.

- *Information 2.0 (1)*
Description: Social media and app links, including icons leading to social media platforms, apps, or newsletters. This does not include forms.
Example: A Twitter icon linking to an official social media page.

- *Interaction (2)*
Description: Communication methods, such as contact details (email, phone numbers, addresses) appearing in the header, footer, or main content. This does not include forms.
Example: A company’s contact section with an email address and phone number.

- *Transaction 1.0 (Indication) (3)*
Description: Indication of a transaction, such as a link to a page containing an e-service or form, without the transaction itself occurring on the current page.
Example: A button leading to an external booking page within the same domain.

- *Transaction 2.0 (4)*
Description: Interrupted transactions that require an action outside the website, such as downloading and submitting a form or uploading files.
Example: A PDF form that users must print, fill out, and send in.

- *Transaction 3.0 (5)*
Description: Uninterrupted transactions that are fully online, such as e-forms, shopping, service bookings, or appointment scheduling.
Example: An online checkout process or an electronic form submission.

- *Integration 1.0 (Indication) (6)*
Description: Promotion of third-party e-services, such as links to external e-services not provided by the website itself.
Example: A link to an external passport application website.

- *Integration 2.0 (7)*
Description: Provision of third-party online services directly integrated within the website.
Example: A municipality website allowing users to book a hut through an integrated third-party service.

- *None of the above classifications (8)*