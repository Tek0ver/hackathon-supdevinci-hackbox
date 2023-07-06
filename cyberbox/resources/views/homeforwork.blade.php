<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Cyberbox</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
        <!-- CSS de Bootstrap -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        

        <!-- php -->
        @php
            $size = 5; // Définissez la taille du tableau ici (par exemple, 5)
        @endphp

        <style>
            /*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */html{line-height:1.15;-webkit-text-size-adjust:100%}body{margin:0}a{background-color:transparent}[hidden]{display:none}html{font-family:system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;line-height:1.5}*,:after,:before{box-sizing:border-box;border:0 solid #e2e8f0}a{color:inherit;text-decoration:inherit}svg,video{display:block;vertical-align:middle}video{max-width:100%;height:auto}.bg-white{--bg-opacity:1;background-color:#fff;background-color:rgba(255,255,255,var(--bg-opacity))}.bg-gray-100{--bg-opacity:1;background-color:#f7fafc;background-color:rgba(247,250,252,var(--bg-opacity))}.border-gray-200{--border-opacity:1;border-color:#edf2f7;border-color:rgba(237,242,247,var(--border-opacity))}.border-t{border-top-width:1px}.flex{display:flex}.grid{display:grid}.hidden{display:none}.items-center{align-items:center}.justify-center{justify-content:center}.font-semibold{font-weight:600}.h-5{height:1.25rem}.h-8{height:2rem}.h-16{height:4rem}.text-sm{font-size:.875rem}.text-lg{font-size:1.125rem}.leading-7{line-height:1.75rem}.mx-auto{margin-left:auto;margin-right:auto}.ml-1{margin-left:.25rem}.mt-2{margin-top:.5rem}.mr-2{margin-right:.5rem}.ml-2{margin-left:.5rem}.mt-4{margin-top:1rem}.ml-4{margin-left:1rem}.mt-8{margin-top:2rem}.ml-12{margin-left:3rem}.-mt-px{margin-top:-1px}.max-w-6xl{max-width:72rem}.min-h-screen{min-height:100vh}.overflow-hidden{overflow:hidden}.p-6{padding:1.5rem}.py-4{padding-top:1rem;padding-bottom:1rem}.px-6{padding-left:1.5rem;padding-right:1.5rem}.pt-8{padding-top:2rem}.fixed{position:fixed}.relative{position:relative}.top-0{top:0}.right-0{right:0}.shadow{box-shadow:0 1px 3px 0 rgba(0,0,0,.1),0 1px 2px 0 rgba(0,0,0,.06)}.text-center{text-align:center}.text-gray-200{--text-opacity:1;color:#edf2f7;color:rgba(237,242,247,var(--text-opacity))}.text-gray-300{--text-opacity:1;color:#e2e8f0;color:rgba(226,232,240,var(--text-opacity))}.text-gray-400{--text-opacity:1;color:#cbd5e0;color:rgba(203,213,224,var(--text-opacity))}.text-gray-500{--text-opacity:1;color:#a0aec0;color:rgba(160,174,192,var(--text-opacity))}.text-gray-600{--text-opacity:1;color:#718096;color:rgba(113,128,150,var(--text-opacity))}.text-gray-700{--text-opacity:1;color:#4a5568;color:rgba(74,85,104,var(--text-opacity))}.text-gray-900{--text-opacity:1;color:#1a202c;color:rgba(26,32,44,var(--text-opacity))}.underline{text-decoration:underline}.antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.w-5{width:1.25rem}.w-8{width:2rem}.w-auto{width:auto}.grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}@media (min-width:640px){.sm\:rounded-lg{border-radius:.5rem}.sm\:block{display:block}.sm\:items-center{align-items:center}.sm\:justify-start{justify-content:flex-start}.sm\:justify-between{justify-content:space-between}.sm\:h-20{height:5rem}.sm\:ml-0{margin-left:0}.sm\:px-6{padding-left:1.5rem;padding-right:1.5rem}.sm\:pt-0{padding-top:0}.sm\:text-left{text-align:left}.sm\:text-right{text-align:right}}@media (min-width:768px){.md\:border-t-0{border-top-width:0}.md\:border-l{border-left-width:1px}.md\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (min-width:1024px){.lg\:px-8{padding-left:2rem;padding-right:2rem}}@media (prefers-color-scheme:dark){.dark\:bg-gray-800{--bg-opacity:1;background-color:#2d3748;background-color:rgba(45,55,72,var(--bg-opacity))}.dark\:bg-gray-900{--bg-opacity:1;background-color:#1a202c;background-color:rgba(26,32,44,var(--bg-opacity))}.dark\:border-gray-700{--border-opacity:1;border-color:#4a5568;border-color:rgba(74,85,104,var(--border-opacity))}.dark\:text-white{--text-opacity:1;color:#fff;color:rgba(255,255,255,var(--text-opacity))}.dark\:text-gray-400{--text-opacity:1;color:#cbd5e0;color:rgba(203,213,224,var(--text-opacity))}.dark\:text-gray-500{--tw-text-opacity:1;color:#6b7280;color:rgba(107,114,128,var(--tw-text-opacity))}}
        </style>

        <style>
            body {
                font-family: 'Nunito', sans-serif;
            }
            table {
                border-collapse: collapse;
                width: 100%;
            }
            
            th, td {
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            
            tr:hover {
                background-color: #ddd;
            }
                    .center-content {
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }
    .select-bar-container {
        margin-bottom: 20px;
    }

    .select-bar {
        width: 300px;
        height: 40px;
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .checkbox-label {
        display: block;
        position: relative;
        padding-left: 35px;
        margin-bottom: 10px;
        cursor: pointer;
        font-size: 16px;
        user-select: none;
    }

    .checkbox-label input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
    }

    .checkmark {
        position: absolute;
        top: 0;
        left: 0;
        height: 20px;
        width: 20px;
        background-color: #eee;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    .checkbox-label:hover input ~ .checkmark {
        background-color: #ccc;
    }

    .checkbox-label input:checked ~ .checkmark {
        background-color: #2196F3;
        border: none;
    }

    .checkbox-label .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }

    .checkbox-label input:checked ~ .checkmark:after {
        display: block;
    }

    .checkbox-label .checkmark:after {
        left: 7px;
        top: 3px;
        width: 6px;
        height: 12px;
        border: solid white;
        border-width: 0 3px 3px 0;
        transform: rotate(45deg);
    }
        </style>
    </head>
    <body class="antialiased">
    <div class="container">
        <div class="row">
            <div class="col-md-3">
                <form method="POST" action="{{ route('search') }}">
                    @csrf
                    <div class="select-bar-container">
                    <select class="select-bar" name="id" size="1" onchange="this.form.submit()">
                        <option value="0" {{ ($clientId == null) ? 'selected' : '' }}>Tous les clients</option>
                        @foreach ($clients as $client)
                            <option value="{{ $client->id }}" {{ ($clientId == $client->id) ? 'selected' : '' }}>{{ $client->entreprise }}</option>
                        @endforeach
                    </select>
                    </div>
                </form>

                <div class="client-tests-container">
                    <div id="clientTestsContainer"></div>
                </div>

                <div class="select-bar-container">
                    @foreach ($machines as $machine)
                        <label class="checkbox-label">
                            <input type="checkbox" name="machines[]" value="{{ $machine->id }}">
                            <span class="checkmark"></span>
                            Machine {{ $machine->id }}
                        </label>
                    @endforeach
                </div>
            </div>
            
            <div class="col-md-6 center-content">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Adresse IP</th>
                            <th>Type</th>
                            <th>Informations</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                    @if ($clientId == 0)
                        <?php $clientasked = $clients; ?>
                    @endif

                        @foreach ($clientasked as $client)
                            @foreach ($client->machines as $machine)
                                @foreach ($machine->tests as $test)
                                    <tr>
                                        <td>{{ $machine->ip }}</td>
                                        <td>{{ $test->type }}</td>
                                        <td>
                                            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalLabel-{{ $test->id }}">
                                                Ouvrir la modale
                                            </button>

                                            <!-- Modale Recon -->
                                            @if ($test->type == "recon")

                                            <div class="modal fade" id="modalLabel-{{ $test->id }}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                                                <div class="modal-dialog" role="document">
                                                    <div class="modal-content">
                                                        <div class="modal-header">
                                                            <h5 class="modal-title" id="modalLabel-{{ $test->id }}">Informations</h5>
                                                            <button type="button" class="close" data-bs-dismiss="modal" aria-label="Fermer">
                                                                <span aria-hidden="true">&times;</span>
                                                            </button>
                                                        </div>
                                                        <div class="modal-body">
                                                            <!-- Contenu de la modale -->
                                                            <?php $jsonData = json_decode($test->result);
                                                            $arrayData = json_decode(json_encode($jsonData), true); ?>
                                                            <table class="table">
                                                            <thead>
                                                                <tr>
                                                                    <th>Host</th>
                                                                    <th>Os</th>
                                                                </tr>
                                                            </thead>
                                                            <tbody>
                                                            @foreach($arrayData["result"] as $dataVal)
                                                            <tr>
                                                                <td>{{$dataVal["host"]}}</td>
                                                                <td>{{$dataVal["os"]}}</td>
                                                            </tr>
                                                            @endforeach
                                                            </tbody>
                                                            </table>
                                                        </div>
                                                        <div class="modal-footer">
                                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            @endif
                                            <!-- End Modale -->

                                            <!-- ----------------------------------------------------------------------------------- -->

                                            <!-- Modale Nmap -->
                                            @if ($test->type == "nmap")

                                            <div class="modal fade" id="modalLabel-{{ $test->id }}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                                                <div class="modal-dialog" role="document">
                                                    <div class="modal-content">
                                                        <div class="modal-header">
                                                            <h5 class="modal-title" id="modalLabel-{{ $test->id }}">Informations</h5>
                                                            <button type="button" class="close" data-bs-dismiss="modal" aria-label="Fermer">
                                                                <span aria-hidden="true">&times;</span>
                                                            </button>
                                                        </div>
                                                        <div class="modal-body">
                                                            <!-- Contenu de la modale -->
                                                            <?php $jsonData = json_decode($test->result);
                                                            $arrayData = json_decode(json_encode($jsonData), true); ?>
                                                            <table class="table">
                                                            <thead>
                                                                <tr>
                                                                    <th>CVE</th>
                                                                    <th>CVSS</th>
                                                                    <th>Service</th>
                                                                    <th>Version</th>
                                                                    <th>Protocole</th>
                                                                </tr>
                                                            </thead>
                                                            <tbody>
                                                            @if (array_key_exists("result", $arrayData))
                                                            @foreach($arrayData["result"] as $dataVal)
                                                            @if (array_key_exists("cve", $dataVal))
                                                            <tr>
                                                                <td>{{$dataVal["cve"]}}</td>
                                                                <td>{{$dataVal["cvss"]}}</td>
                                                                <td>{{$dataVal["service"]}}</td>
                                                                <td>{{$dataVal["version"]}}</td>
                                                                <td>{{$dataVal["protocole"]}}</td>
                                                            </tr>
                                                            @endif
                                                            @endforeach
                                                            @endif
                                                            </tbody>
                                                            </table>
                                                        </div>
                                                        <div class="modal-footer">
                                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            @endif
                                            <!-- End Modale -->

                                        </td>
                                        <td>{{ $test->date }}</td>
                                    </tr>
                                @endforeach
                            @endforeach
                        @endforeach
                    </tbody>
                </table>
            </div>
            <div class="col-md-3">
                <!-- Placez vos boutons ou contenu ici à droite  FAIRE LA CONNEXION ICI-->
            </div>
        </div>
    </div>

    <!-- JavaScript de Bootstrap (facultatif, mais nécessaire pour certaines fonctionnalités de Bootstrap) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>

        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </body>
</html>
